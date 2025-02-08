from django.urls import path
from .views import  lista_paises

urlpatterns = [
   
    path('paises/', lista_paises, name='lista_paises'),
]
