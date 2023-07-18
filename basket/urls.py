from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add_to_basket/<item_id>/',
         views.add_to_basket, name='add_to_basket'),
    path('basket_update/<item_id>/',
         views.basket_update, name='basket_update'),
    path('delete_from_basket/<item_id>/',
         views.delete_from_basket, name='delete_from_basket'),
]
