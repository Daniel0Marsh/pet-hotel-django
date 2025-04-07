from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.duration} - {self.title}'

    class Meta:
        verbose_name = "Prices"
        verbose_name_plural = "Prices"


class WaterSportsPage(TranslatableModel):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    # Non-translatable fields
    hero_image = models.ImageField(upload_to='water_sports/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_watersports_image = models.ImageField(upload_to='water_sports/', blank=True, null=True, default=DEFAULT_IMAGE)

    # Translations for all text fields
    translations = TranslatedFields(
        hero_title=models.CharField(max_length=100, default="Exciting Dog Water Sports Adventures", verbose_name="Hero Title"),
        hero_subheading=models.CharField(
            max_length=255,
            default="Dive into fun with safe, guided aquatic activities designed for dogs of all sizes and skill levels.",
            verbose_name="Hero Subheading"
        ),
        our_watersports_title=models.CharField(max_length=100, default="Fun & Safe Water Activities", verbose_name="Our Water Sports Title"),
        our_watersports_subheading=models.TextField(
            default="From paddle boarding and dock diving to swim training, our experienced team ensures your pup enjoys the water with confidence.",
            verbose_name="Our Water Sports Subheading"
        ),
        watersports_info_title=models.CharField(max_length=100, default="Activities & Packages", verbose_name="Water Sports Info Title"),
        watersports_info_description=models.TextField(
            default="Choose from single-day experiences to multi-session packages. All activities are supervised and tailored to your dog’s comfort and ability level.",
            verbose_name="Water Sports Info Description"
        ),
        cta_title=models.CharField(max_length=100, default="Make a Splash with Us!", verbose_name="CTA Title"),
        cta_subheading=models.TextField(
            default="Book a session today and give your dog the ultimate water adventure. Spots fill fast, so don't miss out!",
            verbose_name="CTA Subheading"
        ),
    )

    class Meta:
        verbose_name = "WaterSports Page Content"
        verbose_name_plural = "WaterSports Page Content"

    def __str__(self):
        return "WaterSports Page Content"
