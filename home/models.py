from django.db import models

# Create your models here.


class Background(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    alt = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    tag = models.SlugField(max_length=250, unique=True)
    number = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='home_images/',
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
        verbose_name_plural = 'backgrounds'


class HomeImg(models.Model):
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