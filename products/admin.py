from django.contrib import admin
from products.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'active')
    list_filter = ('title', 'category')