from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import HomePage, PrivacyPolicyPage, TermsOfServicePage


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


@admin.register(HomePage)
class HomePageAdmin(SingletonAdmin):
    fieldsets = (
        ("Media", {
            "fields": ("video", "hero_image", "about_image", "location_image"),
        }),
        ("Hero Section", {
            "fields": ("hero_title", "hero_subheading"),
        }),
        ("About Section", {
            "fields": ("about_title", "about_subheading"),
        }),
        ("Our Promise Section", {
            "fields": ("promise_title", "promise_subheading"),
        }),
        ("Lifestyle Section", {
            "fields": ("lifestyle_title", "lifestyle_subheading"),
        }),
    )


@admin.register(PrivacyPolicyPage)
class PrivacyPolicyAdmin(SingletonAdmin):
    fields = ("content",)


@admin.register(TermsOfServicePage)
class TermsOfServiceAdmin(SingletonAdmin):
    fields = ("content",)
