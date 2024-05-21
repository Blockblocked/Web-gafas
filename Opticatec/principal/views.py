from django.shortcuts import render
from django.http import HttpResponse
from .  models import Categoria, Producto
def bienvenida(request):
    return render(request, 'bienvenida.html')
# Create your views here.

def productos(request):
    productos = Producto.objects.all()
    categoria =  Categoria.objects.all()
    return render(request, 'vistas/Vproductos.html', {'productos': productos, 'categoria': categoria})

def MasInfo(request):
    return render(request, 'vistas/MasInfo.html')