from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Service(models.Model):
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    fee_per_mile = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Base Price: {self.base_price}, Fee Per Mile: {self.fee_per_mile}"

    class Meta:
        verbose_name = "Prices"
        verbose_name_plural = "Prices"


class TransportationPage(TranslatableModel):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    # Non-translatable fields
    hero_image = models.ImageField(upload_to='transportation/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_transportation_image = models.ImageField(upload_to='transportation/', blank=True, null=True, default=DEFAULT_IMAGE)

    # Translations for all text fields
    translations = TranslatedFields(
        hero_title=models.CharField(max_length=100, default="Reliable Pet Transportation Services", verbose_name="Hero Title"),
        hero_subheading=models.CharField(
            max_length=255,
            default="Safe, comfortable, and stress-free travel for your beloved pets—wherever they need to go.",
            verbose_name="Hero Subheading"
        ),
        our_transportation_title=models.CharField(max_length=100, default="Comfort & Care on the Move", verbose_name="Our Transportation Title"),
        our_transportation_subheading=models.TextField(
            default="Our experienced team ensures every journey is smooth, whether it’s a trip to the vet, airport, or a new home.",
            verbose_name="Our Transportation Subheading"
        ),
        transportation_info_title=models.CharField(max_length=100, default="Services & Routes", verbose_name="Transportation Info Title"),
        training_info_description=models.TextField(
            default="We offer one-way or round-trip transportation options, customizable based on your pet’s needs. Long-distance and local trips available.",
            verbose_name="Transportation Info Description"
        ),
        cta_title=models.CharField(max_length=100, default="Book Safe Pet Travel Today", verbose_name="CTA Title"),
        cta_subheading=models.TextField(
            default="Schedule a ride and travel with peace of mind. Our pet-friendly vehicles and trained staff are ready to help.",
            verbose_name="CTA Subheading"
        ),
    )

    class Meta:
        verbose_name = "Transportation Page Content"
        verbose_name_plural = "Transportation Page Content"

    def __str__(self):
        return "Transportation Page Content"
