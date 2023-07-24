from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('handler404', views.index, name='handler404'),
    path('handler500', views.index, name='handler500'),
]
