from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from parler.admin import TranslatableAdmin
from .models import Service, TransportationPage


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
                reverse(
                    f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                    args=[instance.pk]
                )
            )
        return super().changelist_view(request, extra_context)


@admin.register(TransportationPage)
class TransportationPageAdmin(SingletonAdmin, TranslatableAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(SingletonAdmin):
    list_display = ("base_price", "fee_per_mile")
    list_editable = ("base_price", "fee_per_mile")
    list_display_links = None
