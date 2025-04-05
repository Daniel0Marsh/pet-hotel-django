import json
from datetime import datetime
from decimal import Decimal

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomPrice, Room, Booking, Discount
from django.contrib import messages
from training.models import Service as TrainingService
from water_sports.models import Service as WaterService
from grooming.models import Service as GroomingService
from grooming.models import AnimalSize as GroomingAnimalSize
from meals.models import Service as MealService
from meals.models import AnimalSize as MealAnimalSize
from transportation.models import Transportation
from django.db.models import Sum


class SelectDatesView(TemplateView):
    template_name = 'select_dates.html'

    def post(self, request, *args, **kwargs):
        """Handle actions such as saving dates."""
        action_map = {'save_dates': self.save_dates}
        action = next((key for key in action_map if key in request.POST), None)
        return action_map.get(action, self.invalid_action)(request)

    @staticmethod
    def save_dates(request):
        """Save check-in and check-out dates after validation."""
        check_in_date, check_out_date = request.POST.get('check_in_date'), request.POST.get('check_out_date')

        if not (check_in_date and check_out_date):
            messages.error(request, "Please select both check-in and check-out dates.")
            return render(request, "select_dates.html")

        try:
            check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
            check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
            total_days = (check_out - check_in).days

            if total_days < 1:
                messages.error(request, "Check-out date must be later than check-in date.")
                return render(request, "select_dates.html")

            request.session.update({
                "check_in": check_in_date,
                "check_out": check_out_date,
                "total_days": total_days,
            })
            return redirect("select_room")

        except ValueError:
            messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
            return render(request, "select_dates.html")

    @staticmethod
    def invalid_action(request):
        """Handle invalid actions."""
        return HttpResponse("Invalid action", status=400)


class SelectRoomView(TemplateView):
    template_name = "select_room.html"

    def get(self, request, *args, **kwargs):
        """Redirect to date selection if no rooms are available."""
        if self.check_availability(request) == 0:
            messages.error(request, "No rooms available for the selected date range. Please choose different dates.")
            return redirect("select_dates")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Pass available rooms count, room prices, and total days to the template."""
        context = super().get_context_data(**kwargs)
        context["available_rooms"] = self.check_availability(self.request)
        context["total_days"] = self.request.session.get("total_days")
        context["room_prices"] = RoomPrice.objects.all()

        discount = Discount.objects.first()  # Adjust based on your requirements (e.g., filtering by active status)

        # Add discount values to the context if available
        if discount:
            context["overall_discount"] = discount.overall_discount
            context["multipet_discount"] = discount.multipet_discount
        else:
            context["overall_discount"] = Decimal('0.00')
            context["multipet_discount"] = Decimal('0.00')

        return context

    def post(self, request, *args, **kwargs):
        """Handle actions such as selecting rooms."""
        action_map = {'save_rooms': self.save_rooms}
        action = next((key for key in action_map if key in request.POST), None)
        return action_map.get(action, self.invalid_action)(request)

    @staticmethod
    def check_availability(request):
        """Calculate the number of available rooms."""
        check_in = request.session.get("check_in")
        check_out = request.session.get("check_out")
        total_rooms = Room.objects.count()
        total_pets_in_bookings = Booking.objects.filter(
            check_in_date__lt=check_out, check_out_date__gt=check_in
        ).aggregate(Sum('number_of_pets'))['number_of_pets__sum'] or 0
        return max(total_rooms - total_pets_in_bookings, 0)

    @staticmethod
    def save_rooms(request):
        """Save pet details to session and ensure valid pet count."""
        pets = request.POST.getlist("pet_name[]")
        if not pets:
            messages.error(request, "You must add at least one pet to proceed!")
            return render(request, "select_room.html")

        available_rooms = SelectRoomView.check_availability(request)
        if len(pets) > available_rooms:
            messages.error(request, f"You cannot add more than {available_rooms} pets.")
            return render(request, "select_room.html")

        pet_details = [
            {
                'type': request.POST.getlist('pet_type[]')[i],
                'size': request.POST.getlist('pet_size[]')[i],
                'name': pets[i],
                'breed': request.POST.getlist('pet_breed[]')[i],
                'requirements': request.POST.getlist('pet_requirements[]')[i],
            }
            for i in range(len(pets))
        ]

        request.session["pet_details"] = pet_details
        return redirect("more_details")

    @staticmethod
    def invalid_action(request):
        """Handle invalid actions."""
        return HttpResponse("Invalid action", status=400)


class MoreDetailsView(TemplateView):
    template_name = "more_details.html"

    def get_context_data(self, **kwargs):
        """Return an empty context."""
        return {}

    def post(self, request, *args, **kwargs):
        """Handle actions such as saving details."""
        action_map = {
            'save_details': self.save_details,
        }
        action = next((key for key in action_map if key in request.POST), None)
        return action_map.get(action, self.invalid_action)(request)

    @staticmethod
    def save_details(request):
        """Save details to the session and redirect to the next step."""
        form_data = {
            "full_name": request.POST.get("full_name"),
            "email": request.POST.get("email"),
            "phone_number": request.POST.get("phone_number"),
            "extra_info": request.POST.get("extra_info", ""),
        }

        if all(form_data[field] for field in ["full_name", "email", "phone_number"]):
            request.session.update(form_data)
            return redirect("select_meals")

        messages.error(request, "Please ensure all fields are correct")
        return render(request, "more_details.html")

    @staticmethod
    def invalid_action(request):
        """Handle invalid actions."""
        return HttpResponse("Invalid action", status=400)


class SelectMealsView(TemplateView):
    template_name = "select_meal.html"

    def get_context_data(self, **kwargs):
        """Pass all meal services and their prices to the template."""
        context = super().get_context_data(**kwargs)
        meal_services = MealService.objects.all()

        # Get pet details from session
        pet_details = self.request.session.get("pet_details", [])
        context["meal_services"] = meal_services

        # Loop through each meal service and calculate its price
        for service in meal_services:
            total_price = 0
            for pet in pet_details:
                # Get the price for each pet type and size
                price_obj = MealAnimalSize.objects.filter(
                    animal=pet['type'], size=pet['size'], service=service
                ).first()
                if price_obj:
                    total_price += price_obj.price
            # Attach the price to the service object itself
            service.total_price = total_price

        return context

    def post(self, request, *args, **kwargs):
        """Handle actions such as selecting a meal service or going back."""
        action_map = {
            'meal_service': self.meal_service,
            'go_back': self.go_back,
        }
        action = next((key for key in action_map if key in request.POST), None)
        return action_map.get(action, self.invalid_action)(request)

    @staticmethod
    def meal_service(request):
        """Handle selecting a meal service and saving it to the session."""
        request.session["selected_meal_service"] = request.POST.get("meal_service")
        return redirect("select_transportation")

    @staticmethod
    def go_back(request):
        """Redirect to more details page."""
        return redirect("more_details")

    @staticmethod
    def invalid_action(request):
        """Handle invalid actions."""
        return HttpResponse("Invalid action", status=400)


class SelectTransportationView(TemplateView):
    template_name = "select_transportation.html"

    def get_context_data(self, **kwargs):
        """Pass transportation data to the template."""
        context = super().get_context_data(**kwargs)
        # Assuming you want to pass the first transportation object or handle it otherwise
        transportation = Transportation.objects.first()  # Adjust to handle multiple or specific transportation
        context['transportation'] = transportation
        return context

    def post(self, request, *args, **kwargs):
        """Handle actions such as selecting a room."""
        action_map = {
            'save_address': self.save_address,
            'continue_without': self.continue_without,
        }
        action = next((key for key in action_map if key in request.POST), None)
        return action_map.get(action, self.invalid_action)(request)

    @staticmethod
    def save_address(request):
        """Save the transportation address to the session."""
        address_data = {field: request.POST.get(field, "").strip() for field in
                        ["postcode", "street", "subdistrict", "district", "province", "special_instructions"]}

        # Validate required fields
        missing_fields = [field for field in address_data if
                          field != 'special_instructions' and not address_data[field]]
        if missing_fields:
            messages.warning(request, "Please fill in all required fields before continuing.")
            return render(request, "select_transportation.html")

        request.session["pickup_address"] = address_data
        return redirect("select_grooming")

    @staticmethod
    def continue_without(request):
        """Continue without saving the transportation address."""
        request.session["pickup_address"] = None
        return redirect("select_grooming")

    @staticmethod
    def invalid_action(request):
        """Handle invalid actions."""
        return HttpResponse("Invalid action", status=400)


class SelectGroomingView(TemplateView):
    template_name = "select_grooming.html"

    def get_context_data(self, **kwargs):
        """Pass all grooming services and their prices to the template."""
        context = super().get_context_data(**kwargs)
        grooming_services = GroomingService.objects.all()

        # Get pet details from session
        pet_details = self.request.session.get("pet_details", [])
        context["grooming_services"] = grooming_services

        # Loop through each grooming service and calculate its price
        for service in grooming_services:
            total_price = 0
            for pet in pet_details:
                # Get the price for each pet type and size for grooming
                price_obj = GroomingAnimalSize.objects.filter(
                    animal=pet['type'], size=pet['size'], service=service
                ).first()
                if price_obj:
                    total_price += price_obj.price
            # Attach the price to the service object itself
            service.total_price = total_price

        return context

    def post(self, request, *args, **kwargs):
        """Handle actions for selecting a grooming service."""
        action_map = {
            'grooming_service': self.select_service,
            'continue_without_service': self.continue_without_service,
        }
        action = next((key for key in action_map if key in request.POST), None)
        return action_map.get(action, self.invalid_action)(request)

    @staticmethod
    def select_service(request):
        """Handle selecting a grooming service and saving it to the session."""
        request.session["selected_grooming_service"] = request.POST.get("grooming_service")
        return SelectGroomingView.redirect_based_on_pet(request)

    @staticmethod
    def continue_without_service(request):
        """Continue without selecting a grooming service."""
        request.session["selected_grooming_service"] = None
        return SelectGroomingView.redirect_based_on_pet(request)

    @staticmethod
    def redirect_based_on_pet(request):
        """Redirect based on whether there is a dog in the pet details."""
        pet_details = request.session.get("pet_details", [])
        next_view = "select_training" if any(pet['type'].lower() == 'dog' for pet in pet_details) else "confirm_booking"
        return redirect(next_view)

    @staticmethod
    def invalid_action(request):
        """Handle invalid actions."""
        return HttpResponse("Invalid action", status=400)


class SelectTrainingView(TemplateView):
    template_name = "select_training.html"

    def get_context_data(self, **kwargs):
        """Pass all training services to the template."""
        context = super().get_context_data(**kwargs)
        context["training_services"] = TrainingService.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        """Handle actions for selecting a training service."""
        action_map = {
            'training_service': self.select_service,
            'continue_without_service': self.continue_without_service,
        }
        action = next((key for key in action_map if key in request.POST), None)
        return action_map.get(action, self.invalid_action)(request)

    @staticmethod
    def select_service(request):
        """Handle selecting a training service and saving it to the session."""
        request.session["selected_training_service"] = request.POST.get("training_service")

        next_view = "select_water_sports" if request.session.get("number_of_dogs") else "select_meals"
        return redirect(next_view)

    @staticmethod
    def continue_without_service(request):
        """Continue to the next view without selecting a training service."""
        pet_details = request.session.get("pet_details", [])
        next_view = "select_water_sports" if any(
            pet['type'].lower() == 'dog' for pet in pet_details) else "select_meals"
        return redirect(next_view)

    @staticmethod
    def invalid_action(request):
        """Handle invalid actions."""
        return HttpResponse("Invalid action", status=400)


class SelectWaterSportsView(TemplateView):
    template_name = "select_water_sports.html"

    def get_context_data(self, **kwargs):
        """Pass all water sports services to the template."""
        context = super().get_context_data(**kwargs)
        context["water_sports_services"] = WaterService.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        """Handle actions for selecting a water sports service."""
        action_map = {
            'water_sports_service': self.select_service,
            'continue_without_service': self.continue_without_service,
        }
        action = next((key for key in action_map if key in request.POST), None)
        return action_map.get(action, self.invalid_action)(request)

    @staticmethod
    def select_service(request):
        """Handle selecting a water sports service and saving it to the session."""
        request.session["selected_water_sports_service"] = request.POST.get("water_sports_service")
        return redirect("confirm_booking")

    @staticmethod
    def continue_without_service(request):
        """Continue without selecting a service."""
        return redirect("confirm_booking")

    @staticmethod
    def invalid_action(request):
        """Handle invalid actions."""
        return HttpResponse("Invalid action", status=400)


class ConfirmBookingView(TemplateView):
    template_name = 'confirm_booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        session_data = {key: self.request.session.get(key) for key in [
            "check_in", "check_out", "total_days", "pet_details", "full_name",
            "email", "phone_number", "extra_info", "pickup_address",
            "selected_meal_service", "selected_grooming_service",
            "selected_training_service", "selected_water_sports_service"
        ]}

        prices = {
            "room": 0, "meal": 0, "grooming": 0, "training": 0, "water_sports": 0
        }

        # Calculate prices based on pets and selected services
        for pet in session_data["pet_details"]:
            pet_type, pet_size = pet['type'].lower(), pet['size'].lower()

            # Room price
            room_price = get_object_or_404(RoomPrice, pet_type=pet_type, pet_size=pet_size)
            pet['room_price'] = room_price.price
            prices["room"] += room_price.price * session_data["total_days"]

            # Service prices
            for service_key, service_model, price_key in [
                ("selected_meal_service", MealService, "meal"),
                ("selected_grooming_service", GroomingService, "grooming"),
                ("selected_training_service", TrainingService, "training"),
                ("selected_water_sports_service", WaterService, "water_sports")
            ]:
                service_title = session_data.get(service_key)
                if service_title:
                    service = get_object_or_404(service_model, title=service_title)
                    if price_key == "meal":
                        meal_price = get_object_or_404(MealAnimalSize, animal=pet_type, size=pet_size,
                                                       service=service).price
                        prices[price_key] += meal_price * session_data["total_days"]
                    else:
                        prices[price_key] += service.price

        # Calculate total price before discount
        total_price = sum(Decimal(price) for price in prices.values())

        # Fetch the active discount
        discount = Discount.objects.first()  # Assuming one global discount
        multipet_discount_value = Decimal(0)
        overall_discount_value = Decimal(0)

        if discount:
            # Apply multipet discount if more than one pet is booked
            if len(session_data["pet_details"]) > 1:
                multipet_discount_value = total_price * (discount.multipet_discount / 100)

            # Apply overall discount
            overall_discount_value = total_price * (discount.overall_discount / 100)

        # Total discount applied
        total_discount_value = multipet_discount_value + overall_discount_value

        # Ensure total_discount_value is 0 if no discounts were applied
        if total_discount_value == 0:
            total_discount_value = Decimal(0)

        # Final price after discount
        final_price = total_price - total_discount_value

        # Ensure total_discount_value is 0 if None
        if total_discount_value is None:
            total_discount_value = Decimal(0)

        # Update the context with the values
        context.update({
            **session_data,
            **prices,
            'total_price': total_price,
            'multipet_discount': multipet_discount_value,
            'overall_discount': overall_discount_value,
            'total_discount': total_discount_value,
            'final_price': final_price,
        })

        return context

    def post(self, request, *args, **kwargs):
        action_map = {
            'confirm_booking': self.confirm_booking,
            'go_back': self.go_back,
        }
        action = next((key for key in action_map if key in request.POST), None)
        if action:
            return action_map[action](request)
        return HttpResponse("Invalid action", status=400)

    def confirm_booking(self, request):
        session_data = {key: request.session.get(key) for key in [
            "check_in", "check_out", "full_name", "email", "phone_number",
            "extra_info", "pet_details", "pickup_address",
            "selected_meal_service", "selected_grooming_service",
            "selected_training_service", "selected_water_sports_service", "total_days"
        ]}

        # Calculate the total price (same as in your existing method)
        prices = {
            "room": 0, "meal": 0, "grooming": 0, "training": 0, "water_sports": 0
        }

        for pet in session_data["pet_details"]:
            pet_type, pet_size = pet['type'].lower(), pet['size'].lower()

            # Room price
            room_price = get_object_or_404(RoomPrice, pet_type=pet_type, pet_size=pet_size)
            pet['room_price'] = room_price.price
            prices["room"] += room_price.price * session_data["total_days"]

            # Service prices
            for service_key, service_model, price_key in [
                ("selected_meal_service", MealService, "meal"),
                ("selected_grooming_service", GroomingService, "grooming"),
                ("selected_training_service", TrainingService, "training"),
                ("selected_water_sports_service", WaterService, "water_sports")
            ]:
                service_title = session_data.get(service_key)
                if service_title:
                    service = get_object_or_404(service_model, title=service_title)
                    if price_key == "meal":
                        meal_price = get_object_or_404(MealAnimalSize, animal=pet_type, size=pet_size,
                                                       service=service).price
                        prices[price_key] += meal_price * session_data["total_days"]
                    else:
                        prices[price_key] += service.price

        # Calculate total price before discount
        total_price = sum(Decimal(price) for price in prices.values())

        # Fetch the active discount
        discount = Discount.objects.first()  # Assuming one discount applies globally
        multipet_discount_value = Decimal(0)
        overall_discount_value = Decimal(0)

        if discount:
            # Apply multipet discount if more than one pet is booked
            if len(session_data["pet_details"]) > 1:
                multipet_discount_value = total_price * (discount.multipet_discount / 100)

            # Apply overall discount
            overall_discount_value = total_price * (discount.overall_discount / 100)

        # Total discount applied
        total_discount_value = multipet_discount_value + overall_discount_value

        # Final price after discount
        final_price = total_price - total_discount_value

        # Convert pet details into a readable text format
        pet_details_text = "\n".join([
            f"Pet Type: {pet['type']}, Size: {pet['size']}, Room Price: {pet['room_price']}"
            for pet in session_data["pet_details"]
        ])

        # Handle service selection (fetch actual instances, not strings)
        selected_meal_service = None
        if session_data.get("selected_meal_service"):
            selected_meal_service = get_object_or_404(MealService, title=session_data["selected_meal_service"])

        selected_grooming_service = None
        if session_data.get("selected_grooming_service"):
            selected_grooming_service = get_object_or_404(GroomingService,
                                                          title=session_data["selected_grooming_service"])

        selected_training_service = None
        if session_data.get("selected_training_service"):
            selected_training_service = get_object_or_404(TrainingService,
                                                          title=session_data["selected_training_service"])

        selected_water_sports_service = None
        if session_data.get("selected_water_sports_service"):
            selected_water_sports_service = get_object_or_404(WaterService,
                                                              title=session_data["selected_water_sports_service"])

        # Create booking instance and save the total price
        booking = Booking.objects.create(
            check_in_date=session_data["check_in"],
            check_out_date=session_data["check_out"],
            full_name=session_data["full_name"],
            email=session_data["email"],
            phone_number=session_data["phone_number"],
            extra_info=session_data["extra_info"],
            pickup_address=session_data["pickup_address"],
            selected_meal_service=selected_meal_service,
            selected_grooming_service=selected_grooming_service,
            selected_training_service=selected_training_service,
            selected_water_sports_service=selected_water_sports_service,
            number_of_pets=len(session_data["pet_details"]),
            pet_details=pet_details_text,
            total_price=final_price,
        )

        # Prepare the email content
        email_subject = 'Confirm Your Booking - Luxury Stay'
        email_html = render_to_string('booking_confirmation_email.html', {
            'full_name': session_data["full_name"],
            'email': session_data["email"],
            'phone_number': session_data["phone_number"],
            'extra_info': session_data["extra_info"],
            'check_in_date': session_data["check_in"],
            'check_out_date': session_data["check_out"],
            'pet_details': session_data["pet_details"],
            'selected_meal_service': selected_meal_service,
            'selected_grooming_service': selected_grooming_service,
            'selected_training_service': selected_training_service,
            'selected_water_sports_service': selected_water_sports_service,
            'pickup_address': session_data["pickup_address"],
            'total_price': final_price,
            'meal': prices['meal'],
            'grooming': prices['grooming'],
            'training': prices['training'],
            'water_sports': prices['water_sports'],
            'multipet_discount': multipet_discount_value,
            'overall_discount': overall_discount_value,
            'total_discount': total_discount_value,
            'final_price': final_price,
            'booking_id': booking.id,
            'cancellation_link': request.build_absolute_uri(reverse('cancel_booking', args=[booking.id])),
        })

        # Send email
        send_mail(
            email_subject,
            '',  # Email body (we're using HTML, so this can be left empty)
            settings.DEFAULT_FROM_EMAIL,  # From address
            [session_data["email"]],  # To address
            html_message=email_html,  # HTML content
        )

        return redirect("booking_complete")

    @staticmethod
    def go_back(request):
        pet_details = request.session.get("pet_details", [])
        redirect_url = "select_water_sports" if any(
            pet['type'].lower() == 'dog' for pet in pet_details) else "select_grooming"
        return redirect(redirect_url)


class BookingCompleteView(TemplateView):
    template_name = "booking_complete.html"

    def get_context_data(self, **kwargs):
        """
        Get the context data to display on the confirmation page
        """
        context = super().get_context_data(**kwargs)

        context["email"] = self.request.session.get("email")

        # clear the session
        self.request.session.flush()

        return context


class CancelBooking(TemplateView):
    template_name = "cancel_booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the booking by ID
        booking_id = self.kwargs.get("booking_id")
        booking = get_object_or_404(Booking, booking_id=booking_id)

        # Delete the booking
        booking.delete()

        # Add a message for the user
        context['message'] = f"Your booking with ID {booking_id} has been successfully cancelled and deleted."

        return context
