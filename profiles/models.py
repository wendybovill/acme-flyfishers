import datetime
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User Profile model for maintaining order history
    and other information including delivery
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_title = models.CharField(max_length=80,
                                  null=True, blank=True)

    default_first_name = models.CharField(max_length=100,
                                          null=True, blank=True)

    default_last_name = models.CharField(max_length=100,
                                         null=True, blank=True)

    default_full_name = f'{default_first_name}' + ' ' + f'{default_last_name}'

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
