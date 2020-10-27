from django import forms
from .models import Appointment, UserProfile


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        # only include the fields that are editable by user
        exclude = ('user',)


