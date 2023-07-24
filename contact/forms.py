from django.core.validators import EmailValidator
from django import forms
from .models import ContactForm


class ContactForm(forms.ModelForm):
    """
    A form for submitting contact information and messages.
    """
    class Meta:
        model = ContactForm
        fields = (
            'contact_name',
            'contact_email',
            'contact_phone_number',
            'contact_subject',
            'contact_message',
        )

    def __init__(self, *args, **kwargs):
        """
        Removing labels and using placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Full Name',
            'contact_email': 'Email Address',
            'contact_phone_number': 'Phone Number',
            'contact_subject': 'Subject',
            'contact_message': 'Your Message',
        }

        self.fields['contact_name'].widget.attrs[
            'autofocus'] = True
        self.fields['contact_name'].widget.attrs[
            'aria-label'] = 'Contact name'
        self.fields['contact_email'].widget.attrs[
            'aria-label'] = 'Email Address'
        self.fields['contact_phone_number'].widget.attrs[
            'aria-label'] = 'Phone number'
        self.fields['contact_subject'].widget.attrs[
            'aria-label'] = 'Subject'
        self.fields['contact_message'].widget.attrs[
            'aria-label'] = 'Your message'

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs[
                'placeholder'] = placeholder
            self.fields[field].label = False