from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_item_list = []
    cart_total = 0
    cart_product_count = 0

    cart_session = request.session.get('cart_session', {})

    # item_id is the key and _item_quantity or Item_data \
    # is the value from the sesssion_cart dictionary
    for item_id, item_data in cart_session.items():
        if isinstance(item_data, int):
            cart_product = get_object_or_404(Product, pk=item_id)
            cart_total += item_data * cart_product.price
            cart_product_count += item_data

            cart_item_list.append({
                'item_id': item_id,
                'item_quantity': item_data,
                'cart_product': cart_product,
            })
        else:
            cart_product = get_object_or_404(Product, pk=item_id)
            for product_size, item_quantity in item_data['items_by_size'].items():
                cart_total += item_quantity * cart_product.price
                cart_product_count += item_quantity
                cart_item_list.append({
                    'item_id': item_id,
                    'item_quantity': item_data,
                    'cart_product': cart_product,
                    'product_size': product_size,
                })

    delivery_cost = \
        cart_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery_cost + cart_total

    context = {
        'cart_item_list': cart_item_list,
        'cart_total': cart_total,
        'cart_product_count': cart_product_count,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return context
