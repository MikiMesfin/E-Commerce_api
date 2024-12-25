from django.contrib import admin
from .models import Product, Category, Review, ProductImage, Wishlist, Promotion

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'stock_quantity', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    search_fields = ['name']

admin.site.register([Review, ProductImage, Wishlist, Promotion])
