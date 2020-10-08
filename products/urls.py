from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.display_all_products, name='products')
]