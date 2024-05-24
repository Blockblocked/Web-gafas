from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.MasInfo, name='MasInfo'), 
    path('bievenida', views.bienvenida, name='bienvenida'),
    path('productos',views.productos, name='productos'),
]