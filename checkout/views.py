from django.shortcuts import render, redirect, reverse,\
     get_object_or_404,  HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem, Order
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

#  import the cart_contents view
from cart.contexts import cart_contents

import stripe
import json


@require_POST
# add to the Stripe's payment intent the bag, save info and user info data
def cache_checkout_data(request):
    try:
        payment_intent_id =\
            request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(payment_intent_id, metadata={
            'cart_session':
                json.dumps(request.session.get('cart_session', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):

    if not request.user.is_authenticated:
        messages.info(request,
                       'Please signup or login to your account \
                        in order to complete your purchase')
        return redirect(reverse('account_signup'))

    #  set the public and secret keys variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart_session = request.session.get('cart_session', {})

        #  get data from checkout form
        #  order_form = OrderForm(request.POST)
        form_data = {
            'customer_fullname': request.POST['customer_fullname'],
            'customer_email': request.POST['customer_email'],
            'customer_phone': request.POST['customer_phone'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        #  confirm validity
        if order_form.is_valid():
            order = order_form.save(commit=False)
            payment_int_id = \
                request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = payment_int_id
            order.original_cart = json.dumps(cart_session)
            # remember: upon saving the order_form,
            # the model method _generate_order_number executes
            order = order_form.save()

            # proceed to create OrderLineItem model(s)
            for item_id, item_data in cart_session.items():
                try:
                    cart_product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order_id=order,
                            product=cart_product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for product_size, item_quantity in \
                                item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order_id=order,
                                product=cart_product,
                                quantity=item_quantity,
                                product_size=product_size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't"
                            "found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('display_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request,
                           'There was an error with your form. \
                               Please double check your information.')
    else:
        cart_session = request.session.get('cart_session', {})
        if not cart_session:
            # djandgo's messages to return message (displayed in toast)
            messages.error(request, "Your Shopping Cart is empty!")
            return redirect(reverse('products'))

        # get the cart_content view's context
        checkout_cart_contents = cart_contents(request)
        checkout_grand_total = checkout_cart_contents['grand_total']
        # convert to Integer to satisfy STRIPE's request
        stripe_grand_total = round(checkout_grand_total * 100)
        stripe.api_key = stripe_secret_key
        # Create the Payment Intent required by and to send to Stripe
        # Ref. Stripe documentation and CI's project example
        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_grand_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any
        # info the user maintains in their profile

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                    Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': payment_intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = \
        request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if str(request.user) == 'AnonymousUser':
        order.user_profile = None
    else:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
    order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.customer_phone,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.customer_email}.')

    if 'cart_session' in request.session:
        del request.session['cart_session']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

