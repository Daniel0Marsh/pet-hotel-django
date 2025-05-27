from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Service(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField(),
    )

    def __str__(self):
        # Fetch the title in the current active language
        return self.safe_translation_getter('title', default='No title available')

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"


    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"


class AnimalSize(models.Model):
    SIZE_CHOICES = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )

    ANIMAL_CHOICES = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    )

    animal = models.CharField(max_length=50, choices=ANIMAL_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.get_animal_display()} - {self.get_size_display()} - {self.service.title}'

    class Meta:
        verbose_name = "Prices"
        verbose_name_plural = "Prices"


class GroomingPage(TranslatableModel):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    translations = TranslatedFields(
        hero_title=models.CharField(max_length=100, default="Professional Pet Grooming Services"),
        hero_subheading=models.CharField(max_length=255, default="Keep your furry friend looking and feeling their best with our expert grooming care."),
        our_grooming_title=models.CharField(max_length=100, default="Tailored Grooming for Every Pet"),
        our_grooming_subheading=models.TextField(default="We provide breed-specific grooming, coat care, and spa treatments designed to suit your pet’s individual needs."),
        grooming_info_title=models.CharField(max_length=100, default="Grooming Packages & Pricing"),
        grooming_info_description=models.TextField(default="Choose from full-service grooms, quick clean-ups, or luxury spa packages. Pricing depends on pet size, coat type, and selected services."),
        cta_title=models.CharField(max_length=100, default="Time for a Fresh Look?"),
        cta_subheading=models.TextField(default="Schedule your pet’s grooming session today and give them the pampering they deserve."),
    )

    hero_image = models.ImageField(upload_to='grooming/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_grooming_image = models.ImageField(upload_to='grooming/', blank=True, null=True, default=DEFAULT_IMAGE)

    def __str__(self):
        return "Grooming Page Content"

    class Meta:
        verbose_name = "Grooming Page Content"
        verbose_name_plural = "Grooming Page Content"
