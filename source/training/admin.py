from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "price")
    search_fields = ("title",)
    list_editable = ("price", "duration")
    list_display_links = ("title",)
