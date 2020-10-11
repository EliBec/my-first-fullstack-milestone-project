from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    delivery_cost = \
        total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery_cost + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return context
