from django import template

register = template.Library()


@register.filter(name='item_subtotal')
def item_subtotal(price, quantity):
    return price * quantity
