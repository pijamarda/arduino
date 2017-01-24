from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.utils import timezone

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