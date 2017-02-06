from django.db import models
from django.contrib import admin

# Create your models here.

class TemperaturaTest(models.Model):
    #Este dato sera aportado directamente por el servidor
    fecha = models.DateTimeField('Fecha')
    #Temperatura, en pricipio con formato 23.12
    temperatura = models.DecimalField('Temperatura', max_digits=5, decimal_places=2)
    

class Temperatura(models.Model):
    #Este dato sera aportado directamente por el servidor
    fecha = models.DateTimeField('Fecha')
    #Temperatura, en pricipio con formato 23.12
    temperatura = models.DecimalField('Temperatura', max_digits=5, decimal_places=2)
    #por ejemplo Las Matas, Valdemoro, Torrelavega, etc
    localizacion = models.CharField('localizacion', max_length=20)
    #dentro de una casa por ejemplo, la buhardilla, el sotano, el jardin
    ubicacion = models.CharField('ubicacion', max_length=50)
    #para en un futuro quizas diferenciar los datos subidos por usuario, etc
    usuario = models.CharField('usuario', max_length=15)
    # El id del sensor, en este caso la MAC address
    sensor_id = models.CharField('sensor_id', max_length=30)
    # El ip del sensor
    ip_sensor = models.GenericIPAddressField('ip_sensor', protocol='both', default='0.0.0.0')

