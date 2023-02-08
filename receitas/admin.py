from django.contrib import admin
from . import models
# Register your models here.

# forma de registrar o model na admin
@admin.register(models.Receita) 


class CategoriaAdmin(admin.ModelAdmin): 
    ...



class ReceitasAdmin(admin.ModelAdmin):
    ...



# segunda opção de registrar model no admin
admin.site.register(models.Categoria, CategoriaAdmin) 
