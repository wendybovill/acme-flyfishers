from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.template import RequestContext
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Entry, Section
from django.conf import settings
from django.template.loader import render_to_string

"""
Defining the Home Page for the website, as well as pages
to handle the errors for 404, and 500 http errors
"""


def index(request):

    entries = Entry.objects.all()
    sections = Section.objects.all()

    context = {
        'entries': entries,
        'sections': sections
    }

    return render(request, 'home/index.html', context)


def handler403(request):
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
