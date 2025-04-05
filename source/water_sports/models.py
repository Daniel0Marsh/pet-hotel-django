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
