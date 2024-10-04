from django.contrib import admin
from .models import BlogModel


@admin.register(BlogModel)
class AdminBlogModel(admin.ModelAdmin):
    list_display = ("id", "title",)
