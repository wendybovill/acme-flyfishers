from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

# Create your views here.


def index(request):

    return render(request, 'home/index.html')
