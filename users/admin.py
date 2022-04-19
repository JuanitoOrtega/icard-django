from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Registramos nuestro modelo de usuario en el admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
