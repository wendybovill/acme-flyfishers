from django.db import models
from django.contrib import admin
from django.utils.html import html, mark_safe


class Section(models.Model):
    """
    A model for the Superuser admin to edit the home page of the website
    They can add their own title, they can add various information to
    the index page which serves as a template. There is the option to 
    use html sections or not. Each section has the option to add a 
    background colour, change the text colours, and the content on the
    page. The view displayed on the home page currently does not use
    The section moodel, but it is using the Entry Model.
    """
    name = models.CharField(max_length=250, null=True, blank=True)
    section = models.CharField(max_length=250, null=True, blank=True)
    no = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='section_images/',
                              null=True, blank=True)
    paddingtop = models.CharField(max_length=25, null=True, blank=True)
    paddingbottom = models.CharField(max_length=25, null=True, blank=True)
    paddingleft = models.CharField(max_length=25, null=True, blank=True)
    paddingright = models.CharField(max_length=25, null=True, blank=True)
    backgroundcolor = models.CharField(max_length=50, null=True, blank=True)
    textcolor = models.TextField(max_length=20, null=True, blank=True)
    has_image = models.BooleanField(null=False, blank=False, default=False)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def image_preview1(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "150"/>')

    def image_preview2(self):
        return mark_safe(f'<img src = "{self.image_url.url}" width = "150"/>')

    class Meta:
        verbose_name_plural = 'sections'


class Entry(models.Model):
    """
    A model for the Superuser admin to edit the home page of the website
    They can add their own title, they can add various information to
    the index page which serves as a template. There is the option
    to add Entries to the page, without needing to use sections.
    A section fits the page width 100%, whereas an entry is style,
    and fits the page according to the entry option chosen.
    The view of the Index/Home page is using the entries inserted
    into it as a template, that were placed in the entries from
    the superuser admin section.
    """

    name = models.CharField(max_length=250, null=True, blank=True)
    heading1 = models.CharField(max_length=250, null=True, blank=True)
    heading2 = models.CharField(max_length=250, null=True, blank=True)
    heading3 = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='entry_images/',
                              null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    startercontent = models.TextField(max_length=500, null=True, blank=True)
    blockquote = models.TextField(max_length=500, null=True, blank=True)
    maincontent = models.TextField(max_length=500, null=True, blank=True)
    bulletpoint1 = models.TextField(max_length=500, null=True, blank=True)
    bulletpoint2 = models.TextField(max_length=500, null=True, blank=True)
    bulletpoint3 = models.TextField(max_length=500, null=True, blank=True)
    bulletpoint4 = models.TextField(max_length=500, null=True, blank=True)
    bulletpoint5 = models.TextField(max_length=500, null=True, blank=True)
    endcontent = models.TextField(max_length=500, null=True, blank=True)
    has_image = models.BooleanField(null=False, blank=False, default=False)
    has_image_url = models.BooleanField(null=False, blank=False, default=False)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)
    section = models.ForeignKey(Section, related_name='entry', null=True,
                                blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def image_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "150"/>')

    def image_preview(self):
        return mark_safe(f'<img src = "{self.image_url.url}" width = "150"/>')

    class Meta:
        verbose_name_plural = 'entries'
