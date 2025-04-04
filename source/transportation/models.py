from django.db import models


class Transportation(models.Model):
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    fee_per_mile = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Base Price: {self.base_price}, Fee Per Mile: {self.fee_per_mile}"
