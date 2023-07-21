import datetime
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from django.utils.html import html, mark_safe
from django.conf import settings


class UserProfile(models.Model):
    """
    User Profile model for maintaining order history
    and other information including delivery
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    default_full_name = models.CharField(max_length=100,
                                         null=True, blank=True)

    default_email = models.EmailField(max_length=254,
                                      null=True, blank=True)

    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)

    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)

    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)

    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)

    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)

    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)

    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    User profile creation or updating
    """
    if created:
        UserProfile.objects.create(user=instance)
    # If user already exists then the profile is updated (saved)
    instance.userprofile.save()


class ProfileContactForm(models.Model):
    """
    A form for the registered user to contact the shop owners
    """
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, blank=True,
                             related_name='full_name')

    response = models.BooleanField(blank=True, null=True, default=False)

    default_full_name = models.CharField(max_length=100,
                                         null=True, blank=True)

    default_email = models.EmailField(max_length=254,
                                      null=True, blank=True)

    user_email_subject = models.CharField(max_length=100,
                                          null=False, blank=False)

    user_email_message = models.TextField(max_length=2000,
                                                    null=False,blank=False)

    user_contact_phone_number = models.CharField(max_length=20,
                                                blank=True,null=True)

    image = models.ImageField(upload_to='email_images/',
                              null=True, blank=True)

    image_url = models.URLField(max_length=1024, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.default_email_address

    def image_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "150"/>')

    def get_friendly_name(self):
        return self.default_email
