from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):

    stripe_public_key = 'pk_test_BMSjJHnihRzjkqWU1xf91MuP'

    cart_session = request.session.get('cart_session', {})
    if not cart_session:
        # use djandgo message to return (which is displayed in toast)
        messages.error(request, "Your Shopping Cart is empty!")
        return redirect(reverse('products'))
    else:
        #  instatiate the imported OrderForm
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': 'test_client_secret',
        }
        return render(request, template, context)
