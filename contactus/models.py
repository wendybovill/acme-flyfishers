import datetime
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from django.utils.html import html, mark_safe
from django.conf import settings


class ContactUsForm(models.Model):
    """
    A form for the user to contact the shop owners
    """
    contactus_full_name = models.CharField(max_length=75,
                                           null=False, blank=False)

    contactus_email_address = models.EmailField(max_length=254,
                                                null=False, blank=False)

    contactus_email_subject = models.CharField(max_length=100,
                                               null=False, blank=False)

    contactus_phone_number = models.CharField(max_length=20,
                                              blank=True, null=True)

    contactus_email_message = models.TextField(max_length=1500,
                                               null=False, blank=False)

    date = models.DateTimeField(auto_now_add=True)

    response = models.BooleanField(null=True, blank=True,
                                   default=False)

    def __str__(self):
        return self.contactus_email_address
