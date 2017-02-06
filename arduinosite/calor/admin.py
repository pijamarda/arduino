from django.contrib import admin

from . models import TemperaturaTest, Temperatura
# Register your models here.
admin.site.register(TemperaturaTest)
class TemperaturaAdmin(admin.ModelAdmin):    
    list_display = ('fecha', 'temperatura')
admin.site.register(Temperatura, TemperaturaAdmin)

