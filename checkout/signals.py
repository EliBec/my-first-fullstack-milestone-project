from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

"""
post_save is django's model signal which triggers
at the time of the "save" (updating  or creating a model)
event and executes after the "save" event completes
"""


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order_id.update_total()


"""
post_delete is also a signal which triggers during the "delete" event
(deleting a model) and executes after the event completes
"""


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order_id.update_total()
