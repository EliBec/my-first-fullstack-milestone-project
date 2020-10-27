from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.customer_email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
            handles stripe events other than succeeded or failed
        """
        return HttpResponse(
            content=f'Unhandled received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
            handles stripe payment_intent.succeeded webhook
        """

        intent = event.data.object
        # print(intent)
        payment_int_id = intent.id
        # metadata is a special key in the Stripe payment intent
        cart_session = intent.metadata.cart_session
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = \
                    shipping_details.address.line1
                profile.default_street_address2 = \
                    shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    customer_fullname__iexact=shipping_details.name,
                    customer_email__iexact=billing_details.email,
                    customer_phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart_session,
                    stripe_pid=payment_int_id,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)

            return HttpResponse(
                content=f'Webhook received: {event["type"]} \
                    | SUCCESS: Verified order already in database',
                status=200)

        else:
            order = None
            try:
                order = Order.objects.create(
                    customer_fullname=shipping_details.name,
                    user_profile=profile,
                    customer_email=billing_details.email,
                    customer_phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart_session,
                    stripe_pid=payment_int_id,
                )
                for item_id, item_data in json.loads(cart_session).items():
                    cart_product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order_id=order,
                            product=cart_product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for product_size, item_quantity in\
                             item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order_id=order,
                                product=cart_product,
                                quantity=item_quantity,
                                product_size=product_size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} \
                | SUCCESS: Created order in webhook',
            status=200)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
            handles stripe payment_intent.payment webhook
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


