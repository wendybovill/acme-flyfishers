from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    tag = models.SlugField(max_length=250, unique=True)
    discount = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/products/',
                              null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    season = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

        def __str__(self):
            return self.name


class Product(models.Model):
    sku = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, related_name='products', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    tag = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/products/',
                              null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    colours = models.CharField(max_length=250, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    special_offer = models.BooleanField(verbose_name='Offer',
                                        default=False, null=False, blank=False)
    product_group = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'products'

        def __str__(self):
            return self.title
