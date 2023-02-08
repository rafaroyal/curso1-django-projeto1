from django.urls import path
from . import views

app_name = 'receitas'

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('<int:id>/', views.receitas, name='receita'),
]
