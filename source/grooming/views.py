from django.shortcuts import render
from django.views.generic import TemplateView
from branding.models import Branding
from .models import Service, GroomingPage


class GroomingView(TemplateView):
    template_name = 'grooming.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the hotel page, including discounted room prices.
        """
        context = super().get_context_data(**kwargs)


        context = {
            "branding": Branding.objects.first(),
            "service": Service.objects.all(),
            "grooming": GroomingPage.objects.first(),
        }

        return context
