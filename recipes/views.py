from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Nayra',
        'age': 30,
        'profission': 'Desenvolvedora',
    })


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(response):
    return HttpResponse('Sobre')
    ...
