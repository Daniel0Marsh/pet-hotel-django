# models.py
from django.db import models


class ContactPage(models.Model):
    title = models.CharField(
        max_length=255,
        default="Get in Touch"
    )
    subheading = models.CharField(
        max_length=255,
        blank=True,
        default="We’d love to hear from you! Feel free to reach out with any questions or inquiries."
    )
    image = models.ImageField(
        upload_to="contact/",
        blank=True,
        null=True,
        default="default/placeholder.jpg"
    )

    def __str__(self):
        return "Contact Page Settings"
