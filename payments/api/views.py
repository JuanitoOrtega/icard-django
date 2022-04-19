from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from payments.models import Payment
from payments.api.serializers import PaymentSerializer

# No creamos permisos para el modelo Order, ya que cualquier usuario puede crear una orden.
class PaymentApiViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['table', 'status_payment']
    ordering_fields = '__all__'