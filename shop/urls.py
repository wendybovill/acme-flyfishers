from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:product_id>/', views.view_product, name='view_product')
]