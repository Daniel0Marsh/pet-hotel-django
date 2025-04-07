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


class MealsPage(TranslatableModel):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    # Non-translatable fields
    hero_image = models.ImageField(upload_to='meals/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_meals_image = models.ImageField(upload_to='meals/', blank=True, null=True, default=DEFAULT_IMAGE)

    # Translations for all text fields
    translations = TranslatedFields(
        hero_title=models.CharField(max_length=100, default="Nutritious Meals for Your Pets", verbose_name="Hero Title"),
        hero_subheading=models.CharField(max_length=255, default="Delicious, healthy options tailored to your pet's needs.", verbose_name="Hero Subheading"),
        our_meals_title=models.CharField(max_length=100, default="Deliciously Tailored", verbose_name="Our Meals Title"),
        our_meals_subheading=models.TextField(default="We offer a variety of nutritious meals for dogs and cats, tailored by size and dietary requirements.", verbose_name="Our Meals Subheading"),
        meals_info_title=models.CharField(max_length=100, default="Meal Options & Pricing", verbose_name="Meals Info Title"),
        meals_info_description=models.TextField(default="From premium kibble to gourmet cooked meals, we cater to all sizes and breeds. Pricing varies based on animal size.", verbose_name="Meals Info Description"),
        cta_title=models.CharField(max_length=100, default="Ready to Treat Your Pet?", verbose_name="CTA Title"),
        cta_subheading=models.TextField(default="Book your pet's stay and include their favorite meals today.", verbose_name="CTA Subheading"),
    )

    class Meta:
        verbose_name = "Meals Page Content"
        verbose_name_plural = "Meals Page Content"

    def __str__(self):
        return "Meals Page Content"
