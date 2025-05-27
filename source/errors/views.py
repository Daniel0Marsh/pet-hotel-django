from django.views.generic import TemplateView
from branding.models import Branding
from services.models import Service


class Handler400View(TemplateView):
    """Custom handler for HTTP 400 Bad Request errors."""

    template_name = '400.html'

    def get_context_data(self, **kwargs):
        """
        Return context data for the 400 error page.

        Includes branding and service information.
        """
        context = super().get_context_data(**kwargs)
        context.update({
            "branding": Branding.objects.first(),
            "services": Service.objects.all(),
        })
        return context


class Handler403View(TemplateView):
    """Custom handler for HTTP 403 Forbidden errors."""

    template_name = '403.html'

    def get_context_data(self, **kwargs):
        """
        Return context data for the 403 error page.

        Includes branding and service information.
        """
        context = super().get_context_data(**kwargs)
        context.update({
            "branding": Branding.objects.first(),
            "services": Service.objects.all(),
        })
        return context


class Error404View(TemplateView):
    """Custom handler for HTTP 404 Not Found errors."""

    template_name = '404.html'

    def get_context_data(self, **kwargs):
        """
        Return context data for the 404 error page.

        Includes branding and service information.
        """
        context = super().get_context_data(**kwargs)
        context.update({
            "branding": Branding.objects.first(),
            "services": Service.objects.all(),
        })
        return context


class Handler500View(TemplateView):
    """Custom handler for HTTP 500 Internal Server errors."""

    template_name = '500.html'

    def get_context_data(self, **kwargs):
        """
        Return context data for the 500 error page.

        Includes branding and service information.
        """
        context = super().get_context_data(**kwargs)
        context.update({
            "branding": Branding.objects.first(),
            "services": Service.objects.all(),
        })
        return context
