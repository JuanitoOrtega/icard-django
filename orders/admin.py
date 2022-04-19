from django.contrib import admin
from orders.models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('table', 'product', 'status', 'created_at', 'close', 'note')
    list_filter = ('table', 'status', 'product', 'created_at')
    search_fields = ('table', 'product')