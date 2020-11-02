from django.shortcuts import render


def custome404(request, exception):
    return render(request, "404.html", status=404)


def custom500(request):
    return render(request, "500.html", status=500)