from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.display_cart, name='display_cart')
]
