from django.core.validators import EmailValidator
from django import forms
from .models import ContactUsForm
from .widgets import CustomClearableFileInput

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contactus_full_name': 'Full Name',
            'contactus_email_address': 'Email Address',
            'contactus_email_subject': 'Subject',
            'contactus_email_message': 'Message',
            'contactus_contact_phone_number': 'Phone Number',
            'image': 'Upload Image',
            'image_url': 'Link to Image',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        self.fields['default_full_name'].widget.attrs[
            'aria-label'] = 'Full Name'
        self.fields['default_email'].widget.attrs[
            'aria-label'] = 'Email Address'
        self.fields['user_email_subject'].widget.attrs[
            'aria-label'] = 'Subject'
        self.fields['user_email_message'].widget.attrs[
            'aria-label'] = 'Message'
        self.fields['user_contact_phone_number'].widget.attrs[
            'aria-label'] = 'Phone Number'
        self.fields['image'].widget.attrs[
            'aria-label'] = 'Upload Image'
        self.fields['image_url'].widget.attrs[
            'aria-label'] = 'Link to Image'

        forms.ImageField(label='Image',
                         required=False,
                         widget=CustomClearableFileInput)

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
        self.fields[field].label = False
