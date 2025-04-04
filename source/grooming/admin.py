from django.contrib import admin
from .models import Service, AnimalSize


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(AnimalSize)
class AnimalSizeAdmin(admin.ModelAdmin):
    list_display = ("animal", "size", "service", "price")
    list_filter = ("animal", "size", "service")
    search_fields = ("service__title",)
    list_editable = ("price",)
    list_display_links = ("animal", "size", "service")
