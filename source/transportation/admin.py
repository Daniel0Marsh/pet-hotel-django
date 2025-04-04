from django.contrib import admin
from .models import Transportation


@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ("base_price", "fee_per_mile")
    list_editable = ("base_price", "fee_per_mile")
    list_display_links = None
