from django.db import models
from django.utils.html import html, mark_safe

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    tag = models.SlugField(max_length=250, unique=True)
    discount = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='category_images/',
                              null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def image_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "150"/>')

    class Meta:
        verbose_name_plural = 'categories'


class Season(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'seasons'


class Product(models.Model):
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    hooksize = models.CharField(max_length=50, null=True, blank=True)
    tag = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='product_images/',
                              null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    colours = models.CharField(max_length=250, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    specialoffer = models.BooleanField(null=False, blank=False, default=False)
    multipleproducts = models.CharField(
                                         max_length=1024,
                                         null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    season = models.ForeignKey(Season, related_name='products', null=True,
                               blank=True, on_delete=models.SET_NULL)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def image_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "150"/>')

    class Meta:
        verbose_name_plural = 'products'


class Slide(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    alt = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    tag = models.SlugField(max_length=250, unique=True)
    number = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='slide_images/',
                              null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    caption = models.CharField(max_length=250, null=True, blank=True)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def image_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "150"/>')

    def image_path(self):
        return mark_safe(f'<a href="{self.image.url}">{self.image.url}</a>')

    class Meta:
        verbose_name_plural = 'slides'
