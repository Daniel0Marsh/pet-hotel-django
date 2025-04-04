from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Branding


from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Branding


class SingletonAdmin(admin.ModelAdmin):
    """
    Base admin configuration for singleton models.
    Prevents adding multiple instances and redirects to the existing instance.
    """

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def changelist_view(self, request, extra_context=None):
        instance = self.model.objects.first()
        if instance:
            return HttpResponseRedirect(
                reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change", args=[instance.pk])
            )
        return super().changelist_view(request, extra_context)


@admin.register(Branding)
class BrandingAdmin(SingletonAdmin):
    fieldsets = (
        ("Company Info", {
            "fields": ("company_name", "company_email", "company_phone", "company_address"),
        }),
        ("Brand Assets", {
            "fields": ("logo", "favicon"),
        }),
        ("SEO Metadata", {
            "fields": ("meta_keywords", "meta_description"),
        }),
        ("Social Media Links", {
            "fields": ("twitter_link", "facebook_link", "instagram_link"),
        }),
    )

