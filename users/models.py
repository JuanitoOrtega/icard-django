from django.db import models
from django.contrib.auth.models import AbstractUser

# Creamos nuestro modelo para usuarios
class User(AbstractUser):
    # Sustituimos el campo username por el campo email
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []