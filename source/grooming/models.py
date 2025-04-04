from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


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
        return f'{self.get_animal_display()} - {self.get_size_display()} - {self.service.name}'
