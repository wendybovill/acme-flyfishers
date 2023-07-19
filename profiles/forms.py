from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
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
            'user_title': 'Title',
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email': 'Email Address',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_county': 'County, State or Locality',
            'default_phone_number': 'Phone Number',
        }

        self.fields['user_title'].widget.attrs[
            'aria-label'] = 'Title'
        self.fields['default_first_name'].widget.attrs[
            'aria-label'] = 'First Name'
        self.fields['default_last_name'].widget.attrs[
            'aria-label'] = 'Last Name'
        self.fields['default_email'].widget.attrs[
            'aria-label'] = 'Email Address'
        self.fields['default_street_address1'].widget.attrs[
            'aria-label'] = 'Street Address 1'
        self.fields['default_street_address2'].widget.attrs[
            'aria-label'] = 'Street Address 2'
        self.fields['default_town_or_city'].widget.attrs[
            'aria-label'] = 'Town or City'
        self.fields['default_county'].widget.attrs[
            'aria-label'] = 'County or State'
        self.fields['default_postcode'].widget.attrs[
            'aria-label'] = 'Post Code'
        self.fields['default_country'].widget.attrs[
            'aria-label'] = 'Country'
        self.fields['default_phone_number'].widget.attrs[
            'aria-label'] = 'Phone Number'

        self.fields['user_title'].widget.attrs['autofocus'] = True

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
        self.helper = FormHelper()
        self.fields[field].label = False
