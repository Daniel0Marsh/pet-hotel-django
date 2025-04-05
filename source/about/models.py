from django.db import models


class AboutPage(models.Model):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    # Hero Section
    hero_title = models.CharField(
        max_length=200,
        default="About Us"
    )
    hero_subheading = models.TextField(
        default="Where every paw is pampered and every whisker welcomed. Experience exceptional care in a serene, home-away-from-home setting."
    )
    hero_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE
    )

    # Our Story Section
    our_story_title = models.CharField(
        max_length=200,
        default="Our Story"
    )
    our_story_subheading = models.TextField(
        default="What began as a dream to create the perfect haven for pets quickly became a reality. Built on love, trust, and comfort, our space is designed to offer pets a holiday of their own."
    )
    our_story_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE
    )

    # Our Mission Section
    our_mission_title = models.CharField(
        max_length=200,
        default="Our Mission"
    )
    our_mission_subheading = models.TextField(
        default="To provide a tranquil and enriching environment where pets are nurtured, loved, and treated with the utmost care — every single day."
    )
    our_mission_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE
    )

    # Our Team Section
    our_team_title = models.CharField(
        max_length=200,
        default="Meet the Team"
    )
    our_team_subheading = models.TextField(
        default="A passionate team of animal lovers, professional caregivers, and trained staff, all dedicated to making pets feel safe, happy, and right at home."
    )
    our_team_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE
    )

    # Our Commitment Section
    our_commitment_title = models.CharField(
        max_length=200,
        default="Our Commitment"
    )
    our_commitment_subheading = models.TextField(
        default="We’re devoted to setting a new standard in pet hospitality — luxurious spaces, personalized care, and a loving environment for every furry guest."
    )
    our_commitment_image = models.ImageField(
        upload_to='about/',
        default=DEFAULT_IMAGE
    )

    def __str__(self):
        return "About Page Content"

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"
