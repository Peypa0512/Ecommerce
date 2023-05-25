# para la app de Usuarios crearemos también este fichero
from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.usuariolist, name="usuario_list")
]
