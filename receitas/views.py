from django.shortcuts import render
from . import models
# from django.http import HttpResponse
# Create your views here.


def home(request):
    receitas = models.Receita.objects.all()
    res = render(request, 'receitas/paginas/receitas-home.html', context={
        'receita': receitas
    })
    return res

def categoria(request, categoria_id):
    receitas = models.Receita.objects.filter(categoria__id=categoria_id)
    res = render(request, 'receitas/paginas/receitas-home.html', context={
        'receita': receitas
    })
    return res


def receitas(request, id):
    res = render(request, 'receitas/paginas/receita-view.html', context={
        'nome': 'Rafael'
    })
    return res
