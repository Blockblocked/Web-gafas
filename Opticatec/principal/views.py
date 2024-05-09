from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request):
    return render(request, 'bienvenida.html')
# Create your views here.
