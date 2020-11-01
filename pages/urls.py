from django.urls import path
from . import views  # . means current directory


urlpatterns = [
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
]
