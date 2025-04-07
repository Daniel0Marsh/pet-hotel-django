from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from parler.admin import TranslatableAdmin
from .models import ContactPage


class SingletonAdmin(admin.ModelAdmin):
    """
    Base admin configuration for singleton models.
    Prevents adding multiple instances and redirects to the existing instance.
    """

    def has_add_permission(self, request):
        # Prevents adding a new instance of the singleton model
        return not self.model.objects.exists()

    def changelist_view(self, request, extra_context=None):
        instance = self.model.objects.first()
        if instance:
            # Redirect to the existing instance change form
            return HttpResponseRedirect(
                reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change", args=[instance.pk])
            )
        return super().changelist_view(request, extra_context)


@admin.register(ContactPage)
class ContactPageAdmin(SingletonAdmin, TranslatableAdmin):
    """
    Admin for ContactPage that integrates Parler for translations.
    Inherits SingletonAdmin to ensure only one instance exists.
    """
    pass
