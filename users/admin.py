from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

# Registramos nuestro modelo de usuario en el admin
# Esta clase se crea después de crear, ejecutar las migraciones y después de crear el superuser
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)