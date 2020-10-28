from django import forms
from .models import Appointment, UserProfile


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        # only include the fields that are editable by user
        fields = ('customer_fullname', 'customer_phone', 'customer_email',
                 'appointment_date', 'appointment_time', 'reason', 'notes',)


    def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'customer_fullname': 'Full Name',
                'customer_phone': 'Phone Number',
                'customer_email': 'Email Address',
                'appointment_date': 'yyyy/mm/dd',
                'appointment_time': '0:00 a.m',
                'reason': 'Reason for Service',
                'notes': 'Any details you would like to share',
            }

            self.fields['customer_fullname'].widget.attrs['autofocus'] = True
            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
