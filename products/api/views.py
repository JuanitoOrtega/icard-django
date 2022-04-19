from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly # Si está autenticado le da todos los permisos, si no, solo le da permisos de lectura.
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product
from products.api.serializers import ProductSerializer

class ProductApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category', 'active'] # Esto es para filtrar por nombre y por categoría.