from django.contrib import admin
from .models import Appointment


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'customer_fullname',
        'customer_phone',
        'customer_email',
        'appointment_time',
        'appointment_date',
        'created_date',
        'created_time',
        'notes',
        'reason',
    )

    ordering = ('appointment_date',)


admin.site.register(Appointment, AppointmentAdmin)
