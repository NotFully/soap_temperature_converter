from django.db import models


class TemperatureConversion(models.Model):
    celsius = models.DecimalField(max_digits=5, decimal_places=2)
    fahrenheit = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        self.fahrenheit = (self.celsius * 9/5) + 32
        super().save(*args, **kwargs)
