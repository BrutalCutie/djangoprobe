from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ("id", "name", "category")


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("id", "name",)
