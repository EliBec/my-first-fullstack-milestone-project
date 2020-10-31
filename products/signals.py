from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Rating


@receiver(post_save, sender=Rating)
def update_on_save(sender, instance, created, **kwargs):
    print("Request saved!")
    instance.product.update_rating()


@receiver(post_delete, sender=Rating)
def update_on_delete(sender, instance, **kwargs):
    print("Request delete!")
    instance.product.update_rating()
