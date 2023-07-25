from django.db import models
from django.conf import settings


class ContactForm(models.Model):
    """
    This model is for a site visitors and
    logged in users to send a contact form
    to shop admins
    """
    contact_name = models.CharField(
        max_length=75, null=False, blank=False)
    contact_email = models.EmailField(
        max_length=254, null=False, blank=False)
    contact_subject = models.CharField(
        max_length=100, null=False, blank=False)
    contact_message = models.TextField(
        max_length=1500, null=False, blank=False)
    contact_phone_number = models.CharField(
        max_length=20, blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.contact_email
