from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from projects.models import Product, Cart

class ProductAdmin(admin.ModelAdmin):
    pass

class CartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin) 
admin.site.register(Cart, CartAdmin)