import json, random, decimal

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.utils import timezone

from .models import TemperaturaTest

def index(request):

    template = loader.get_template('calor/index.html')
    tiempo = timezone.now()
    temperaturas = TemperaturaTest.objects.all().order_by('fecha')   

    data_temp = []
    data_fecha = []
    for t in temperaturas:
        data_temp.append(float(t.temperatura))
        data_fecha.append((t.fecha).strftime("%Y-%m-%d %H:%M:%S"))

    context = {
        'tiempo': tiempo,
        'temperaturas': temperaturas,
        'data_temp': data_temp,
        'data_fecha': data_fecha,
    }
    return HttpResponse(template.render(context,request))

def api_index(request):

    template = loader.get_template('calor/index.html')
    return HttpResponse(template.render(request))

def add_temp_test(request):

    print('estoy dentro de la funcion')
    # Primero nos traemos desde el GET las nuevas variables a modificar

    random_temp = float(decimal.Decimal(random.randrange(10000))/100)
    if request.method == 'GET':
        data = TemperaturaTest.objects.create(temperatura=random_temp, fecha=timezone.now())
        print('estoy dentro de GET')

    
    response = {'fecha': data.fecha.strftime('%Y %m %d %H:%M:%S'), 
                'temperatura': data.temperatura,
                }
    return HttpResponse(json.dumps( response ), content_type="application/json")

def add_temp(request):
    return HttpResponse('hola')