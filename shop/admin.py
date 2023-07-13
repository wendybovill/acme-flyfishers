from django.contrib import admin
from .models import Category, Product, Slide

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


class SlideAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview', 'image_path']
    list_display = (
        'name',
        'number',
        'title',
        'image',
        'image_url',
        'alt',
        'tag',
        'caption',
    )

    ordering = ('number',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slide, SlideAdmin)
