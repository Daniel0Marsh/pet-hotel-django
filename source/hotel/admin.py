from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from parler.admin import TranslatableAdmin
from .models import HotelPage, ServicePage


class SingletonAdmin(admin.ModelAdmin):
    """
    Base admin configuration for singleton models.
    Prevents adding multiple instances and redirects to the existing instance.
    """

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def changelist_view(self, request, extra_context=None):
        instance = self.model.objects.first()
        if instance:
            return HttpResponseRedirect(
                reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change", args=[instance.pk])
            )
        return super().changelist_view(request, extra_context)


@admin.register(HotelPage)
class HotelPageAdmin(SingletonAdmin, TranslatableAdmin):
    """
    Admin for HotelPage model that integrates Parler for translations.
    """
    pass


@admin.register(ServicePage)
class ServicePageAdmin(SingletonAdmin, TranslatableAdmin):
    """
    Admin for ServicePage model that integrates Parler for translations.
    """
    pass
