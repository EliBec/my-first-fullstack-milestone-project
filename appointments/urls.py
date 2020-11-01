from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.display_appointments, name='appointments'),
    path('display_appointment_detail/<appointment_number>',
         views.display_appointment_detail, name='display_appointment_detail'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
]
