from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

"""
post_save is django's model signal which triggers
at the time of the "save" (updating  or creating a model)
event and executes after the "save" event happens
"""


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


"""
post_save is also a django's model signal which
triggers at the time of the "delete"
(deleting a model) event and executes
after the "delete" event happens
"""


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
 
    instance.order.update_total()
