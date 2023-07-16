from django.contrib import admin
from .models import Category, Product, Slide, Season

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


class SeasonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview',]
    list_display = (
        'name',
        'image',
        'image_url',
        'sku',
        'price',
        'stock',
        'category',
        'tag',
        'friendly_name',
        'description',
        'hook_size',
        'colours',
        'discount',
        'special_offer',
        'multiple_products',
        'season',
    )

    ordering = ('name',)


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
admin.site.register(Season, SeasonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slide, SlideAdmin)
