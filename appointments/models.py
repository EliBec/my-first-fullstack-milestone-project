import uuid

from django.db import models
from .utils import Preference as Pref
from profiles.models import UserProfile

# Create your models here.


class Appointment(models.Model):
    number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True,
                                     on_delete=models.SET_NULL,
                                     related_name='appointments')
    customer_fullname = \
        models.CharField(max_length=50, null=False, blank=False)
    customer_phone =  \
        models.CharField(max_length=20, null=False, blank=False)
    customer_email =  \
        models.EmailField(max_length=254, null=False, blank=False)
    appointment_time = models.TimeField(null=False, blank=False, auto_now=False, auto_now_add=False)
    appointment_date = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False)
    created_date = models.DateField(auto_now=True, auto_now_add=False)
    created_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    notes = models.TextField(null=True, blank=True)
    reason = models.CharField(max_length=15, choices=Pref.reason_list)

    #  model method
    def _generate_appointment_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    """
    returns the value in the name attrib of the Product class
    which will be displayed in the Django admin pannel.
    """
    def __str__(self):
        return f'Appointment for {self.customer_fullname} on \
                                 {self.appointment_date} at \
                                 {self.appointment_time} '
