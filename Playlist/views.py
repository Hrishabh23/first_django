from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def helloWorld(request):
    return HttpResponse("Hello World")

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())