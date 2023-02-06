from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    res = render(request, 'receitas/home.html', context={
        'nome': 'Rafael'
    })
    return res


def sobre(request):
    res = HttpResponse('sobre')
    return res


def contato(request):
    res = HttpResponse("contato")
    return res
