from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Entry, Section
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.


def index(request):

    entries = Entry.objects.all()
    sections = Section.objects.all()

    context = {
        'entries': entries,
        'sections': sections
    }

    return render(request, 'home/index.html', context)
