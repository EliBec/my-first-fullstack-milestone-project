from django.shortcuts import render


# Create your views here.
def services(request):

    welcome_msg = 'Services!'

    context = {
        'welcome_msg': welcome_msg
    }

    return render(request, 'pages/our_services.html', context)


def about(request):

    welcome_msg = 'About us!'

    context = {
        'welcome_msg': welcome_msg,
    }

    return render(request, 'pages/about_us.html', context)

