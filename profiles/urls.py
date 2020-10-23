from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.user_profile, name='profiles'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]