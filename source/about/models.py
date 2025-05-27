from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class AboutPage(TranslatableModel):
    """
    Model representing translatable content for the 'About' page.

    This model supports multiple languages using django-parler,
    and includes section-specific titles, subheadings, and images.
    """

    DEFAULT_IMAGE = 'default/placeholder.jpg'

    translations = TranslatedFields(
        hero_title=models.CharField(
            max_length=200,
            default="About Us",
            help_text="Title text for the hero section."
        ),
        hero_subheading=models.TextField(
            default="Where every paw is pampered and every whisker welcomed. "
                    "Experience exceptional care in a serene, home-away-from-home setting.",
            help_text="Subheading text for the hero section."
        ),
        our_story_title=models.CharField(
            max_length=200,
            default="Our Story",
            help_text="Title for the 'Our Story' section."
        ),
        our_story_subheading=models.TextField(
            default="What began as a dream to create the perfect haven for pets quickly became a reality. "
                    "Built on love, trust, and comfort, our space is designed to offer pets a holiday of their own.",
            help_text="Subheading for the 'Our Story' section."
        ),
        our_mission_title=models.CharField(
            max_length=200,
            default="Our Mission",
            help_text="Title for the 'Our Mission' section."
        ),
        our_mission_subheading=models.TextField(
            default="To provide a tranquil and enriching environment where pets are nurtured, loved, and treated with "
                    "the utmost care — every single day.",
            help_text="Subheading for the 'Our Mission' section."
        ),
        our_team_title=models.CharField(
            max_length=200,
            default="Meet the Team",
            help_text="Title for the 'Our Team' section."
        ),
        our_team_subheading=models.TextField(
            default="A passionate team of animal lovers, professional caregivers, and trained staff, all dedicated to "
                    "making pets feel safe, happy, and right at home.",
            help_text="Subheading for the 'Our Team' section."
        ),
        our_commitment_title=models.CharField(
            max_length=200,
            default="Our Commitment",
            help_text="Title for the 'Our Commitment' section."
        ),
        our_commitment_subheading=models.TextField(
            default="We’re devoted to setting a new standard in pet hospitality — luxurious spaces, personalized care, "
                    "and a loving environment for every furry guest.",
            help_text="Subheading for the 'Our Commitment' section."
        ),
    )

    # Image fields for corresponding sections
    hero_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE,
        help_text="Image for the hero section."
    )
    our_story_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE,
        help_text="Image for the 'Our Story' section."
    )
    our_mission_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE,
        help_text="Image for the 'Our Mission' section."
    )
    our_team_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE,
        help_text="Image for the 'Our Team' section."
    )
    our_commitment_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE,
        help_text="Image for the 'Our Commitment' section."
    )

    def __str__(self):
        """String representation of the AboutPage instance."""
        return "About Page Content"

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"
