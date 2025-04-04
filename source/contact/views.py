from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
import requests
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from branding.models import Branding
from .models import ContactPage


class ContactPageView(TemplateView):
    """
    View for rendering the contact page.

    Attributes:
        template_name (str): Name of the template file to be used.
    """
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the template.

        Returns:
            dict: Context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            "contact": ContactPage.objects.first(),
        }
        return context

    @staticmethod
    def post(request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        captcha_response = request.POST.get('g-recaptcha-response')

        # Verify reCAPTCHA
        captcha_data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': captcha_response
        }
        captcha_verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        response = requests.post(captcha_verify_url, data=captcha_data)
        result = response.json()

        if result.get('success') and name and email and message:
            # Send the email if CAPTCHA is valid
            subject = f"Contact Us Message from {name}"

            def send_email(recipient_email):
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=email,
                    recipient_list=[recipient_email],
                    fail_silently=False,
                )

            # Send email to the main contact email
            send_email(settings.CONTACT_EMAIL)

            # Send email to all registered users
            users = User.objects.all()
            for user in users:
                if user.email:
                    send_email(user.email)

            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect(request.path)

        # If CAPTCHA failed or data is missing, show an error
        messages.error(request, "There was an issue sending your message. Please try again.")
        return render(request, 'contact_us.html')
