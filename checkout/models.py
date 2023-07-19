import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from shop.models import Product
from profiles.models import UserProfile
from django.utils.html import html, mark_safe


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    full_name = f'{first_name}' + ' ' + f'{last_name}'
    email = models.EmailField(max_length=254, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=False, default=0)
    full_total = models.DecimalField(max_digits=10, decimal_places=2,
                                     null=False, default=0)
    grand_total = full_total
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Create order number based on customers uuid
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Change total of order when a new lineitem is added, including delivery
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        sdp = settings.STANDARD_DELIVERY_PERCENTAGE
        self.delivery_cost = self.order_total * sdp / 100
        self.full_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Set the order number in save
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True,
                                    blank=True)  # 8, 10, 12, 14, 16
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')

    def save(self, *args, **kwargs):
        """
        set line total and order total on save
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Item {self.product.name} on order {self.order.order_number}'
