from django.views.generic import TemplateView
from .models import AboutPage
from branding.models import Branding


class AboutView(TemplateView):
    """
    View to render the About page.

    Provides context data including branding and about page content.
    """

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        """
        Return context data for the about page template.

        Adds branding and about page content to the context.

        Args:
            **kwargs: Arbitrary keyword arguments passed to the view.

        Returns:
            dict: Context dictionary for rendering the template.
        """
        context = super().get_context_data(**kwargs)
        context.update({
            "branding": Branding.objects.first(),
            "about": AboutPage.objects.first(),
        })
        return context
