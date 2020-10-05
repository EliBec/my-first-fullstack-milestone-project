from django.shortcuts import render


# Create your views here.
def welcome(request):

    welcome_msg = 'Welcome to Beck!'

    # template = "home/index.html"

    context = {
        'welcome_msg': welcome_msg
    }

    return render(request, 'home/index.html', context)
