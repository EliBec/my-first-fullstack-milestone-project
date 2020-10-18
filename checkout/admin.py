# Register your models here.
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created_date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'created_date', 'customer_fullname',
              'customer_email', 'customer_phone', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'created_date', 'customer_fullname',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    """
    sorting. must be a dupple. Add -
    next to the field name for reverse sorting
    """
    ordering = ('-created_date',)


admin.site.register(Order, OrderAdmin)
