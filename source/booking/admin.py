from django.contrib import admin
from .models import Room, RoomPrice, Discount, Booking


@admin.register(RoomPrice)
class RoomPriceAdmin(admin.ModelAdmin):
    list_display = ("pet_type", "pet_size", "price")
    list_filter = ("pet_type", "pet_size")
    search_fields = ("pet_type", "pet_size")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "created_at")
    search_fields = ("number",)
    ordering = ("number",)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("overall_discount", "multipet_discount")
    list_editable = ("overall_discount", "multipet_discount")
    list_display_links = None  # Allow direct editing in the list view


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "check_in_date", "check_out_date", "number_of_pets", "total_price")
    search_fields = ("full_name", "email", "phone_number")
    list_filter = ("check_in_date", "check_out_date")
    ordering = ("-check_in_date",)

    fieldsets = (
        ("Booking Information", {
            "fields": ("full_name", "email", "phone_number", "pickup_address", "extra_info")
        }),
        ("Stay Details", {
            "fields": ("check_in_date", "check_out_date", "number_of_pets", "pet_details")
        }),
        ("Selected Services", {
            "fields": ("selected_meal_service", "selected_grooming_service", "selected_training_service", "selected_water_sports_service"),
            "classes": ("collapse",)
        }),
        ("Pricing", {
            "fields": ("total_price",)
        }),
    )

