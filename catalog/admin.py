from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod_name', 'price',)
    list_filter = ('prod_name',)
    search_fields = ('prod_name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name',)
    list_filter = ('cat_name',)
    search_fields = ('cat_name', 'description')


