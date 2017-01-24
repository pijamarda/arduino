from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.utils import timezone

from .models import TemperaturaTest

def index(request):

    template = loader.get_template('calor/index.html')
    tiempo = timezone.now()
    context = {
        'tiempo': tiempo,
    }
    return HttpResponse(template.render(context,request))

def api_index(request):

    template = loader.get_template('calor/index.html')
    return HttpResponse(template.render(request))

def add_temp_test(request):

    print('estoy dentro de la funcion')	
    # Primero nos traemos desde el GET las nuevas variables a modificar
    if request.method == 'GET':
        TemperaturaTest.objects.create(temperatura=23.4, fecha=timezone.now())
        print('estoy dentro de GET')

    response = 'ok'
    return HttpResponse(response)