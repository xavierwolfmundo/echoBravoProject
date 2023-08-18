from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def order_saved(sender, instance, created, **kwargs):
    if created:
        # Perform any necessary actions when a new order is created
        pass
    else:
        # Perform any necessary actions when an existing order is saved
        pass
