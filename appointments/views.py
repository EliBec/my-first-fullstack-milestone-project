from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from pages.views import services

from .models import Appointment
from profiles.models import UserProfile

from .forms import AppointmentForm


# Create your views here
@login_required
def display_appointments(request):

    if not request.user.is_authenticated:
        messages.info(request, 'Please create or login to your account \
                       in order to see you appointment history.')
        return redirect(reverse('account_signup'))

    # get the user info first
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # to then get the user's past appointments
    appointments = user_profile.appointments.all()

    template = 'appointments/display_appointments.html'

    context = {
        'appointments': appointments,
    }

    return render(request, template, context)


@login_required
def display_appointment_detail(request, appointment_number):

    if not request.user.is_authenticated:
        messages.info(request, 'Please login in order to see \
                       your appointment information.')
        return redirect(reverse('account_signup'))

    appointment = get_object_or_404(Appointment, number=appointment_number)

    template = 'appointments/appointment_detail.html'

    context = {
        "appointment": appointment,
    }

    return render(request, template, context)


# add a new appointment
@login_required
def add_appointment(request):

    if not request.user.is_authenticated:
        messages.info(request, 'Please create or log in to your account \
                       in order to make an appointment.')
        return redirect(reverse('account_signup'))
        #  profile = UserProfile.objects.get(user=request.user)
        #  Attach the user's profile to the apointment

    if request.method == "POST":
        #  instance of the ProductProfileForm based
        #  on the request date from POST
        appointment_form_data = AppointmentForm(request.POST)
        if appointment_form_data.is_valid():
            appointment = appointment_form_data.save()
            messages.success(request, 'Appointment Saved Successfully!')
            return redirect(reverse('display_appointment_detail',
                            args=[appointment.number]))
        else:
            messages.error(request,
                           'Failed to save apointment.'
                           'Please ensure the form is correclty filled.')
    else:
        appointment_form_data = AppointmentForm()

    context = {
        'appointment_form_data': appointment_form_data,
    }

    template = 'appointments/add_appointment.html'

    return render(request, template, context)
