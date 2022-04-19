from django.contrib import admin
from payments.models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'amount', 'payment_type', 'status_payment', 'date')
    list_filter = ('payment_type', 'status_payment', 'table')
    search_fields = ('table', 'payment_type', 'status_payment')