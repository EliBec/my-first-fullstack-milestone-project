from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.user_profile, name='profiles'),
]