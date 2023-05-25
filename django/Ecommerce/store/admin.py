from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # los campos que quiero listar
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    # como quiero generar ciertos campos 'slug'
    prepopulated_fields = {'slug' : ('product_name',)}


admin.site.register(Product, ProductAdmin)
