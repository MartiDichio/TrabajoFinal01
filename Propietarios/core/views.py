from django.http import HttpResponse
from django.shortcuts import render

from .models import Silicon, Point

def silicon_index(request):
    return HttpResponse("Bienvenido a la aplicación Silicon.")

def point_index(request):
    return HttpResponse("Bienvenido a la aplicación Point.")
