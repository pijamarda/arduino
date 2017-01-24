from django.db import models

# Create your models here.

class TemperaturaTest(models.Model):
    fecha = models.DateTimeField('Fecha')
    temperatura = models.DecimalField('Temperatura', max_digits=5, decimal_places=2)