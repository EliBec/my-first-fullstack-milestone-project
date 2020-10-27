from django import template

register = template.Library()

# here we register a custom template filter to use on django templates


@register.filter(name='item_subtotal')
def item_subtotal(price, quantity):
    return price * quantity
