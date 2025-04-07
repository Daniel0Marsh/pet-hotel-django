from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Service(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField(),
    )
    duration = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.safe_translation_getter('title', default='No title available')

    class Meta:
        verbose_name = "Prices"
        verbose_name_plural = "Prices"


class TrainingPage(TranslatableModel):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    # Non-translatable fields
    hero_image = models.ImageField(upload_to='training/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_training_image = models.ImageField(upload_to='training/', blank=True, null=True, default=DEFAULT_IMAGE)

    # Translations for all text fields
    translations = TranslatedFields(
        hero_title=models.CharField(max_length=100, default="Expert Dog Training Services", verbose_name="Hero Title"),
        hero_subheading=models.CharField(max_length=255, default="Professional, compassionate training tailored to your dog's behavior and needs.", verbose_name="Hero Subheading"),
        our_training_title=models.CharField(max_length=100, default="Personalized Dog Training", verbose_name="Our Training Title"),
        our_training_subheading=models.TextField(default="From basic obedience to advanced behavioral correction, our trainers work with dogs of all breeds and sizes.", verbose_name="Our Training Subheading"),
        training_info_title=models.CharField(max_length=100, default="Training Programs & Pricing", verbose_name="Training Info Title"),
        training_info_description=models.TextField(default="We offer flexible programs including group classes, private sessions, and intensive boot camps. Pricing depends on program type and duration.", verbose_name="Training Info Description"),
        cta_title=models.CharField(max_length=100, default="Ready to Train Your Dog?", verbose_name="CTA Title"),
        cta_subheading=models.TextField(default="Book a consultation today and start your dog’s journey to better behavior and obedience.", verbose_name="CTA Subheading"),
    )

    class Meta:
        verbose_name = "Training Page Content"
        verbose_name_plural = "Training Page Content"

    def __str__(self):
        return "Training Page Content"
