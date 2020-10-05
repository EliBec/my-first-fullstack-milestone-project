from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.welcome, name='home')
]
