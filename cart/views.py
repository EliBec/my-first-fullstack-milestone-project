from django.shortcuts import render


# Create your views here.
def display_cart(request):

    cart_msg = "Let's keep shopping!"

    # template = "home/index.html"

    context = {
        'cart_message': cart_msg,
    }

    return render(request, 'cart/cart.html', context)

