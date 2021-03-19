from django.contrib import admin
from .models import Product
from .category import Category


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
