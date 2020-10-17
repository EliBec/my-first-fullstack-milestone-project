from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.display_cart, name='display_cart'),
    path('add_to_cart/<item_id>/', views.add_to_cart,
         name='add_to_cart'),
    path('update_cart_qty/<item_id>/', views.update_cart_qty,
         name='update_cart_qty'),
    path('remove_from_cart/<item_id>/', views.remove_from_cart,
         name='remove_from_cart'),
]
