from django.urls import path
from .views import RegistrarUsuario, IniciarSesion

urlpatterns = [
    path('register/', RegistrarUsuario.as_view(), name='registrar_usuario'),
    path('login/', IniciarSesion.as_view(), name='iniciar_sesion'),
]