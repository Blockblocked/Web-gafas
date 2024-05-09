from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('productos',views.productos, name='productos')
]