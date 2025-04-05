from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from django.db import models


class HomePage(models.Model):
    """
    Model representing the homepage information for the website.

    This model stores essential details such as the site's branding elements,
    contact information, and media assets used on the homepage.
    """

    DEFAULT_IMAGE = "default/placeholder.jpg"
    DEFAULT_VIDEO = "default/placeholder.mp4"

    # FileField for the walkaround video
    video = models.FileField(
        upload_to="home_page/",
        help_text="Upload the walkaround video.",
        default=DEFAULT_VIDEO
    )

    # ImageFields for the homepage images
    hero_image = models.ImageField(
        upload_to="home_page/",
        help_text="Upload the hero section background image.",
        default=DEFAULT_IMAGE
    )
    about_image = models.ImageField(
        upload_to="home_page/",
        help_text="Upload the about section image.",
        default=DEFAULT_IMAGE
    )
    location_image = models.ImageField(
        upload_to="home_page/",
        help_text="Upload the location section image.",
        default=DEFAULT_IMAGE
    )

    # Titles and subheadings for different homepage sections
    hero_title = models.CharField(
        max_length=100,
        help_text="Main title for the hero section.",
        default="Unmatched Comfort for Your Pet"
    )
    hero_subheading = models.CharField(
        max_length=255,
        help_text="Subheading text for the hero section.",
        default="A peaceful, luxury stay designed for ultimate relaxation, fun, and pampering."
    )

    about_title = models.CharField(
        max_length=100,
        help_text="Title for the about section.",
        default="A Place Designed With Pets in Mind"
    )
    about_subheading = models.CharField(
        max_length=255,
        help_text="Subheading for the about section.",
        default="Every corner crafted for safety, joy, and serenity — because they deserve the best."
    )

    promise_title = models.CharField(
        max_length=100,
        help_text="Title for the 'Our Promise' section.",
        default="Our Promise to You"
    )
    promise_subheading = models.CharField(
        max_length=255,
        help_text="Subheading for the 'Our Promise' section.",
        default="Compassionate care, luxurious surroundings, and attention to every detail of your pet’s stay."
    )

    lifestyle_title = models.CharField(
        max_length=100,
        help_text="Title for the lifestyle section.",
        default="The Lifestyle They Deserve"
    )
    lifestyle_subheading = models.CharField(
        max_length=255,
        help_text="Subheading for the lifestyle section.",
        default="Spacious play areas, gourmet meals, spa treatments, and cozy naps — it’s more than a stay, it’s a lifestyle."
    )

    def __str__(self):
        return "Home Page Content"

    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Content"


class PrivacyPolicyPage(models.Model):
    """
    Model representing the privacy policy.
    """
    content = CKEditor5Field(config_name='default', null=True, blank=True)

    def __str__(self):
        return "Privacy Policy Content"

    class Meta:
        verbose_name = "Privacy Policy Content"
        verbose_name_plural = "Privacy Policy Content"


class TermsOfServicePage(models.Model):
    """
    Model representing the terms of service.
    """
    content = CKEditor5Field(config_name='default', null=True, blank=True)

    def __str__(self):
        return "Terms Of Service Page Content"

    class Meta:
        verbose_name = "Terms Of Service Page Content"
        verbose_name_plural = "Terms Of Service Page Content"
