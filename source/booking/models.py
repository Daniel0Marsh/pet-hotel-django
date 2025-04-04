from decimal import Decimal
from django.db import models
from grooming.models import Service as GroomingService
from meals.models import Service as MealService
from training.models import Service as TrainingService
from water_sports.models import Service as WaterService


class RoomPrices(models.Model):
    """Represents the prices of rooms per night."""

    PET_TYPE_CHOICES = [('dog', 'Dog'), ('cat', 'Cat')]
    PET_SIZE_CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]

    pet_type = models.CharField(max_length=50, choices=PET_TYPE_CHOICES)
    pet_size = models.CharField(max_length=50, choices=PET_SIZE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pet_type.capitalize()} - {self.pet_size.capitalize()} - {self.price} per night"


class Room(models.Model):
    """
    Represents each room in the system.
    """
    number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.number}"


class Discount(models.Model):
    """Represents discounts available for rooms and multipet bookings."""
    overall_discount = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'), help_text="Overall discount for all rooms (as a percentage).")
    multipet_discount = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'), help_text="Discount for bookings with multiple pets (as a percentage).")

    def __str__(self):
        return f"Overall Discount: {self.overall_discount}% | Multipet Discount: {self.multipet_discount}%"


class Booking(models.Model):
    """
    Represents each booking in the system.
    """
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    extra_info = models.TextField(null=True, blank=True)
    pickup_address = models.TextField(null=True, blank=True)
    selected_meal_service = models.ForeignKey(MealService, on_delete=models.SET_NULL, null=True, blank=True)
    selected_grooming_service = models.ForeignKey(GroomingService, on_delete=models.SET_NULL, null=True, blank=True)
    selected_training_service = models.ForeignKey(TrainingService, on_delete=models.SET_NULL, null=True, blank=True)
    selected_water_sports_service = models.ForeignKey(WaterService, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_pets = models.IntegerField()
    pet_details = models.JSONField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Booking for {self.full_name} from {self.check_in_date} to {self.check_out_date}"
