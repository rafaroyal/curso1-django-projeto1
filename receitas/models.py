from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField()
    prep_time = models.IntegerField()
    prep_time_unit = models.IntegerField()
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    prep_steps = models.TextField()
    prep_steps_is_html = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='receitas/cover/%Y/%m/%d/', blank=True, default='')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True
    )
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.titulo