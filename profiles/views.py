from django.shortcuts import render, get_object_or_404

from .models import UserProfile


# Create your views here.
def user_profile(request):

    user_profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/userprofile.html'

    context = {
        'user_profile': user_profile,
    }

    return render(request, template, context)
