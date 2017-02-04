import json, random, decimal

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.utils import timezone
from django.utils.timezone import localtime

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

    
    # Primero nos traemos desde el GET las nuevas variables a modificar

    random_temp = float(decimal.Decimal(random.randrange(10000))/100)
    if request.method == 'GET':
        data = TemperaturaTest.objects.create(temperatura=random_temp, fecha=timezone.now())
    
    
    response = {'fecha': localtime(data.fecha).strftime('%Y %m %d %H:%M:%S'), 
                'temperatura': data.temperatura,
                }
    return HttpResponse(json.dumps( response ), content_type="application/json")

def add_temp(request):
    print('estoy dentro de la funcion')
    if request.method == 'GET':
        temp_get = request.GET.get('temp')
        loc_get = request.GET.get('loc')
        ubi_get = request.GET.get('ubi')
        user_get = request.GET.get('user')
        sid_get = request.GET.get('sid')
        sip_get = request.GET.get('sip')
        print(temp_get)
        print(loc_get)
        print(ubi_get)
        print(user_get)
        print(sid_get)
        print(sip_get)
        #data = TemperaturaTest.objects.create(temperatura=temperatura_get, fecha=timezone.now())
        print('estoy dentro de GET')   
    
    return HttpResponse(temp_get)
