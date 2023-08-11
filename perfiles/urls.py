from perfiles.views import *
from django.urls import path, include
from django.contrib import admin

# Agrega esto a la lista de URLs
# URLS de Perfil
urlpatterns = [
    path('registro/', registro, name = 'registro'),
    path('login/', login_view, name = 'login'),
    path('logout/', CustomLogoutView.as_view(), name = 'logout'),
    path('editar-mi-perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
]




