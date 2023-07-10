from django.contrib import admin
from .models import Category, Product

# register


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'tag',
        'discount',
    )

    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'sku',
        'price',
        'category',
        'tag',
        'description',
        'image',
        'image_url',
        'colours',
        'discount',
        'special_offer',
        'product_group',
    )

    ordering = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
