from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add_to_bag/<item_id>/',
         views.add_to_bag, name='add_to_bag'),
    path('bag_update/<item_id>/',
         views.bag_update, name='bag_update'),
    path('delete_from_bag/<item_id>/',
         views.delete_from_bag, name='delete_from_bag'),
]
