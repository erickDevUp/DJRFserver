from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models

class CustomUser(AbstractUser):
    username = None  # Remueve el campo 'username'
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    
    USERNAME_FIELD = 'email'  # Define 'email' como el campo de nombre de usuario
    REQUIRED_FIELDS = []  # Elimina 'username' de los campos requeridos
