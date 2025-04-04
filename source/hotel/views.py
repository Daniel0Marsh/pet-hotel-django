from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HotelPage, ServicePage
from home.models import HomePage
from branding.models import Branding
from booking.models import RoomPrices, Discount
from decimal import Decimal


class HotelView(TemplateView):
    template_name = 'hotel.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the hotel page, including discounted room prices.
        """
        context = super().get_context_data(**kwargs)

        discount = Discount.objects.first()
        room_prices = RoomPrices.objects.all()

        room_prices_with_discount = []
        for room in room_prices:
            original_price = room.price
            discounted_price = None

            if discount and discount.overall_discount > 0:
                discount_amount = (original_price * discount.overall_discount) / Decimal(100)
                discounted_price = original_price - discount_amount

            room_prices_with_discount.append({
                'pet_type': room.pet_type,
                'pet_size': room.pet_size,
                'original_price': original_price,
                'discounted_price': discounted_price,
            })

        context.update({
            "branding": Branding.objects.first(),
            "hotel": HotelPage.objects.first(),
            "room_prices": room_prices_with_discount,  # Updated list with discounted prices
            "discount": discount,
        })

        return context


class ServicesView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the template.

        Returns:
            dict: Context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            "home": HomePage.objects.first(),
            "service": ServicePage.objects.first(),
        }
        return context

