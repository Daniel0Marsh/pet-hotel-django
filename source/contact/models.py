from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class ContactPage(TranslatableModel):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    translations = TranslatedFields(
        title=models.CharField(
            max_length=255,
            default="Get in Touch"
        ),
        subheading=models.CharField(
            max_length=255,
            blank=True,
            default="We’d love to hear from you! Feel free to reach out with any questions or inquiries."
        ),
    )

    image = models.ImageField(
        upload_to="contact/",
        blank=True,
        null=True,
        default=DEFAULT_IMAGE
    )

    def __str__(self):
        return "Contact Page Content"

    class Meta:
        verbose_name = "Contact Page Content"
        verbose_name_plural = "Contact Page Content"
