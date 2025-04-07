from django.shortcuts import render
from django.views.generic import TemplateView
from branding.models import Branding
from .models import Service, WaterSportsPage


class WaterSportsView(TemplateView):
    template_name = 'water_sports.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the hotel page, including discounted room prices.
        """
        context = super().get_context_data(**kwargs)


        context = {
            "branding": Branding.objects.first(),
            "service": Service.objects.all(),
            "watersports": WaterSportsPage.objects.first(),
        }

        return context
