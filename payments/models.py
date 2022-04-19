from django.db import models

PaymentTypeEnum = (
    ('CASH', 'Efectivo'),
    ('CARD', 'Tarjeta'),
    ('TRANSFER', 'Transferencia'),
    ('QR', 'QR')
)

StatusPaymentEnum = (
    ('PENDING', 'Pendiente'),
    ('PAID', 'Pagado')
)

# Create your models here.
class Payment(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=255, choices=PaymentTypeEnum)
    status_payment = models.CharField(max_length=255, choices=StatusPaymentEnum)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.table)