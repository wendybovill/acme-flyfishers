from django.contrib import admin
from .models import ContactUsForm
from .widgets import CustomClearableFileInput


class ContactUsForm(admin.ModelAdmin):
    readonly_fields = ['date',
                       'contactus_contact_phone_number',
                       'contactus_email_subject',
                       'contactus_email_message',
                       'contactus_email_address',]

    list_display = (
        'response',
        'contactus_full_name',
        'contactus_email_address',
        'contactus_email_subject',
        'contactus_email_message',
        'contactus_contact_phone_number'
        'date',
    )

    ordering = ('date',)


admin.site.register(ContactUsForm, ContactUsFormAdmin)
