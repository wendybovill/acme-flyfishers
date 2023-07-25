from django.contrib import admin
from .models import Entry, Section


class EntryAdmin(admin.ModelAdmin):
    """
    The Superuser section with the Entry options for the
    index/home page
    """
    readonly_fields = ['image_preview1', 'image_preview2',]
    list_display = (
        'name',
        'heading1',
        'heading2',
        'heading3',
        'image',
        'image_url',
        'startercontent',
        'blockquote',
        'maincontent',
        'bulletpoint1',
        'bulletpoint2',
        'bulletpoint3',
        'bulletpoint4',
        'bulletpoint5',
        'endcontent',
        'has_image',
        'has_image_url',
        'friendly_name',
    )

    ordering = ('name',)

    admin.site.register(Entry)


class SectionAdmin(admin.ModelAdmin):
    """
    The Superuser section with the Section options for the
    index/home page
    """
    readonly_fields = ['image_preview1', 'image_preview2',]
    list_display = (
        'name',
        'section',
        'no'
        'image'
        'paddingtop'
        'paddingbottom'
        'paddingleft'
        'paddingright'
        'backgroundcolor'
        'textcolor'
        'has_image'
        'friendly_name'
    )

    ordering = ('name',)

    admin.site.register(Section)
