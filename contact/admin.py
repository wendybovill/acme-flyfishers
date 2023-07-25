from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    """
    The fields being used for admin view
    showing display options and if editable
    or not
    """
    readonly_fields = [
        'contact_name',
        'contact_email',
        'contact_phone_number',
        'contact_subject',
        'contact_message',
        'date',
        ]

    list_display = (
        'contact_name',
        'contact_email',
        'contact_subject',
        'contact_message',
        'contact_phone_number',
        'date',
        'responded',
    )

    ordering = ('date',)


admin.site.register(ContactForm, ContactFormAdmin)
