from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutPage
from branding.models import Branding


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the template.

        Returns:
            dict: Context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            "about": AboutPage.objects.first(),
        }
        return context
