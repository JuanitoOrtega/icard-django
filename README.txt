# Creamos nuestro entorno virtual
python3 -m venv env

# Activamos nuestro entorno virtual
source env/bin/activate

# Desactivar entorno virtual
deactivate

# Instalamos django
pip install django

# Actualizamos pip a su última versión
python3 -m pip install --upgrade pip

# Creamos nuestra app icard
django-admin startproject icard

# Lanzamos el servidor
python3 manage.py runserver

# Ejecutamos la migración
python3 manage.py migrate

# Instalamos dependencia para crear nuestra API REST
# https://www.django-rest-framework.org/
pip install djangorestframework

# Instalamos dependencia para crear documentación de nuestra API
# https://drf-yasg.readthedocs.io/en/stable/readme.html#table-of-contents
pip install -U drf-yasg

# Creamos un superusuario para acceder al admin de django
# User: jortega Pass: admin
python3 manage.py createsuperuser

# Ver ayuda
python3 manage.py --help

# Creamos app para gestionar usuarios
python3 manage.py startapp users

# Generamos las migraciones
python3 manage.py makemigrations

# Aplicamos la migración
python3 manage.py migrate

# Cambiar login de usuario a correo electrónico

# Instalamos librería jwt para gestionar login
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
pip install djangorestframework-simplejwt

# Instalamos librería para gestionar el CORS
pip install django-cors-headers

# Creamos nueva app para categorías
python3 manage.py startapp categories

# Instalamos paquete para trabajar con imágenes
pip install Pillow

# Generamos las migraciones
python3 manage.py makemigrations

# Aplicamos la migración
python3 manage.py migrate

# Para conectar con Postgres instalamos la siguiente librería
pip install psycopg2

# Creamos app de productos
python3 manage.py startapp products

- Añadimos la app a settings.py
- Creamos el modelo con los campos requeridos
- Editamos el archivo admin.py de la app products

- Creamos el ModelViewSet
- Creamos carpeta api
- Creamos __init__.py en carpeta api
- Creamos views.py en carpeta api
- Creamos serializers.py en la carpeta api
- Creamos router.py en la carpeta api
- En el archivo urls.py importamos router_product
- En views.py importamos DjangoFilterBackend
- En el archivo serializers.py de productos importamos CategorySerializer

# Generamos las migraciones
python3 manage.py makemigrations

# Aplicamos la migración
python3 manage.py migrate

# Instalamos librería para crear filtros en los modelos
# https://www.django-rest-framework.org/#installation
# https://pypi.org/project/django-filter/
pip install django-filter

- En settings.py, INTALLED_APPS, debajo de 'corsheaders', añadimos 'django_filters'

# Creamos nueva app para gestionar las mesas
python3 manage.py startapp tables

# Agregamos la app tables a la app principal en settings
-- Creamos nuestro modelo en models.py
-- Añadimos la app al dashboard de django editando el archivo admin.py, aquí también definimos qué columnas mostrar, filtros

# Generamos las migraciones
python3 manage.py makemigrations

# Aplicamos las migraciones
python3 manage.py migrate

# Creamos el ModelViewSet de la app Tables
-- Dentro de la raíz principal de la app, creamos la carpeta api, dentro creamos los archivos: __init__.py, views.py
-- Editamos el archivo views.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from tables.models import Table

class TableApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # serializer_class = ...
    queryset = Table.objects.all().order_by('number')

# Creamos el serializador
-- Dentro de api creamos el archivo serializers.py
-- Editamos el archivo serializers.py

from rest_framework.serializers import ModelSerializer
from tables.models import Table

class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        # fields = ['id', 'number']
        fields = '__all__'
    
-- Importamos el serializador en el archivo views.py

# Generamos las rutas
-- Dentro de la carpeta api, creamos el archivo router.py
-- Editamos el archivo router.py e importamos nuestros views

from rest_framework.routers import DefaultRouter
from tables.api.views import TableApiViewSet

router_table = DefaultRouter()

router_table.register(
    prefix='tables', basename='tables', viewset=TableApiViewSet
)

# Agregamos nuestras rutas al archivo urls.py de la app principal
-- Importamos nuestras rutas

//////////////////////////////////////////////////
# Creamos app para los pedidos
python3 manage.py startapp orders

-- 1. Añadimos la app al archivo settings.py de la app principal
-- 2. Creamos el modelo para los pedidos en el archivo models.py de la app orders

StatusEnum = (
    ('PENDING', 'Pendiente'),
    ('DELIVERED', 'Entregado'),
)

# Create your models here.
class Order(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=255, default='PENDING', choices=StatusEnum)
    note = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    close = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table)

-- Añadimos el modelo al dashboard de django editando el archivo admin.py de nuestra app orders

from orders.models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('table', 'product', 'status', 'created_at', 'close', 'note')
    list_filter = ('table', 'status', 'product', 'created_at')
    search_fields = ('table', 'product')

# Generamos las migraciones
python3 manage.py makemigrations

# Aplicamos las migraciones generadas
python3 manage.py migrate

# Para generar el CRUD
-- Todos estos pasos en la carpeta de nuestra app orders
-- Creamos carpeta api
-- Dentro de la carpeta api
-- Creamos archivo vacío __init__.py
-- Creamos archivo serializers.py

from rest_framework.serializers import ModelSerializer
from orders.models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'table', 'product', 'close', 'created_at', 'note']

-- Creamos archivo views.py e importamos OrderSerializer

from rest_framework.viewsets import ModelViewSet
from orders.models import Order
from orders.api.serializers import OrderSerializer

class OrderApiViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

-- Creamos archivo router.py

from rest_framework.routers import DefaultRouter
from orders.api.views import OrderApiViewSet

router_order = DefaultRouter()

router_order.register(
    prefix = 'orders', basename='orders', viewset=OrderApiViewSet
)

-- Nos queda integrar las rutas en urls.py de nuestra app principal
-- Añadimos filtros al view de order, importamos lo siguiente dentro de views.py

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

-- También añadimos a la clase OrderApiViewSet lo siguiente:

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['table', 'status', 'product', 'close']
    ordering_fields = ['__all__']

-- Para que el serializador nos devuelva los datos detallados
-- Editamos en archivo serializers.py y nos importamos lo siguiente

from products.api.serializers import ProductSerializer
from tables.api.serializers import TableSerializer

///////////// PAYMENT SYSTEM /////////////
-- Creamos app payments
python3 manage.py startapp payments

-- Añadimos la nueva a settings de la app principal
-- Creamos el modelo
-- Integramos en admin.py

# Generamos las migraciones
python3 manage.py makemigrations

# Aplicamos las migraciones generadas
python3 manage.py migrate

-- Creamos carpeta api
-- Creamos archivo serializers.py
-- Creamos archivo views.py e importamos nuestro serializador
-- Creamos nuestro archivo router.py e importamos nuestro PaymentApiViewSet
-- Añadimos nuestras rutas al archivo urls.py de nuestra app principal

from payments.api.router import router_payment

-- Con los pasos anteriores el modelo ya debería estar disponible enla documentación de nuestra api

# Añadiendo filtros al modelo
-- Importamos en views.py

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

    ...
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['table', 'status_payment']
    ordering_fields = '__all__'

-- Ahora debemos añadir el modelo Payment al modelo Order mediante ForeignKey

# Generamos las migraciones
python3 manage.py makemigrations

# Aplicamos las migraciones generadas
python3 manage.py migrate