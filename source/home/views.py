from django.views.generic import TemplateView
from .models import HomePage, PrivacyPolicyPage, TermsOfServicePage
from branding.models import Branding
from hotel.models import ServicePage


class HomePageView(TemplateView):
    """
    View for rendering the home page.

    Attributes:
        template_name (str): Name of the template file to be used.
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the template.

        Returns:
            dict: Context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            "home": HomePage.objects.first(),
            "service": ServicePage.objects.first(),
        }
        return context


class PrivacyPolicyPageView(TemplateView):
    """
    View for displaying privacy policy.
    """
    template_name = 'privacy_policy.html'

    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            'privacy_policy': PrivacyPolicyPage.objects.first(),
        }
        return context


class TermsOfServicePageView(TemplateView):
    """
    View for displaying terms of service.
    """
    template_name = 'terms_of_service.html'

    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            'terms_of_service': TermsOfServicePage.objects.first(),
        }
        return context
