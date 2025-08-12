from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(response):
    return HttpResponse('Home 2')
    ...


def contato(response):
    return HttpResponse('Contato')
    ...


def sobre(response):
    return HttpResponse('Sobre')
    ...
