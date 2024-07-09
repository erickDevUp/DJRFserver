from django.urls import path
from .views import RegistrarUsuario, IniciarSesion, Logout

urlpatterns = [
    path('register/', RegistrarUsuario.as_view(), name='registrar_usuario'),
    path('login/', IniciarSesion.as_view(), name='iniciar_sesion'),
    path('logout/', Logout.as_view(), name='logout'),
]