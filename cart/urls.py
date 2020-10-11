from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.display_cart, name='display_cart'),
    path('add_to_cart/<item_id>', views.add_to_cart,
         name='add_to_cart')
]
