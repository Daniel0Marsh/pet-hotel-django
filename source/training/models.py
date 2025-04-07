from django.db import models


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


class TrainingPage(models.Model):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    hero_title = models.CharField(max_length=100, default="Expert Dog Training Services")
    hero_subheading = models.CharField(max_length=255, default="Professional, compassionate training tailored to your dog's behavior and needs.")
    hero_image = models.ImageField(upload_to='training/', blank=True, null=True, default=DEFAULT_IMAGE)

    our_training_title = models.CharField(max_length=100, default="Personalized Dog Training")
    our_training_subheading = models.TextField(default="From basic obedience to advanced behavioral correction, our trainers work with dogs of all breeds and sizes.")
    our_training_image = models.ImageField(upload_to='training/', blank=True, null=True, default=DEFAULT_IMAGE)

    training_info_title = models.CharField(max_length=100, default="Training Programs & Pricing")
    training_info_description = models.TextField(default="We offer flexible programs including group classes, private sessions, and intensive boot camps. Pricing depends on program type and duration.")

    cta_title = models.CharField(max_length=100, default="Ready to Train Your Dog?")
    cta_subheading = models.TextField(default="Book a consultation today and start your dog’s journey to better behavior and obedience.")

    class Meta:
        verbose_name = "Training Page Content"
        verbose_name_plural = "Training Page Content"

    def __str__(self):
        return "Training Page Content"
