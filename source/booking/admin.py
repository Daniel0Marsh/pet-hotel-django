from django.contrib import admin
from .models import Room, RoomPrice, Discount, Booking


@admin.register(RoomPrice)
class RoomPriceAdmin(admin.ModelAdmin):
    """
    Admin configuration for RoomPrice model.

    Displays pricing based on pet type and size.
    """
    list_display = ("pet_type", "pet_size", "price")
    list_filter = ("pet_type", "pet_size")
    search_fields = ("pet_type", "pet_size")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    Admin configuration for Room model.

    Displays room number and creation date.
    """
    list_display = ("number", "created_at")
    search_fields = ("number",)
    ordering = ("number",)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """
    Admin configuration for Discount model.

    Allows editing of discount values directly from the list view.
    """
    list_display = ("overall_discount", "multipet_discount")
    list_editable = ("overall_discount", "multipet_discount")
    list_display_links = None  # Disables linking to the change form for inline editing


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Booking model.

    Organizes fields into sections and improves search and filter functionality.
    """
    list_display = ("full_name", "check_in_date", "check_out_date", "number_of_pets", "total_price")
    search_fields = ("full_name", "email", "phone_number")
    list_filter = ("check_in_date", "check_out_date")
    ordering = ("-check_in_date",)

    fieldsets = (
        ("Booking Information", {
            "fields": ("full_name", "email", "phone_number", "pickup_address", "extra_info"),
        }),
        ("Stay Details", {
            "fields": ("check_in_date", "check_out_date", "number_of_pets", "pet_details"),
        }),
        ("Selected Services", {
            "fields": (
                "selected_meal_service",
                "selected_grooming_service",
                "selected_training_service",
                "selected_water_sports_service"
            ),
            "classes": ("collapse",),
        }),
        ("Pricing", {
            "fields": ("total_price",),
        }),
    )
