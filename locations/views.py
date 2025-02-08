from django.shortcuts import render
from .models import Pais

def lista_paises(request):
    paises = Pais.objects.all()
    return render(request, "locations/paises.html", {"paises": paises})  # Correcto
