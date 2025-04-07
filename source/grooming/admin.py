from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Service, AnimalSize, GroomingPage


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


@admin.register(GroomingPage)
class MealsPageAdmin(SingletonAdmin):
    pass