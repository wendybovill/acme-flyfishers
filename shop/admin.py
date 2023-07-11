from django.contrib import admin
from .models import Category, Product

# register


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview',]
    list_display = (
        'name',
        'friendly_name',
        'tag',
        'discount',
        'image',
        'image_url',
        'description',
    )

    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview',]
    list_display = (
        'image',
        'image_url',
        'title',
        'sku',
        'price',
        'category',
        'tag',
        'description',
        'colours',
        'discount',
        'special_offer',
        'product_group',
    )

    ordering = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
