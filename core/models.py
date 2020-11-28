from django.db import models

# Create your models here.
class PointerMarker(models.Model):
    nome_local = models.CharField(max_length = 100)
    latitude = models.DecimalField(max_digits = 10,decimal_places = 7)
    longitude = models.DecimalField(max_digits = 10, decimal_places = 7)
