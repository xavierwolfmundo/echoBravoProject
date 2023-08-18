from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registration

@receiver(post_save, sender=Registration)
def registration_saved(sender, instance, created, **kwargs):
    if created:
        # Perform any necessary actions when a new registration is created
        pass
    else:
        # Perform any necessary actions when an existing registration is saved
        pass
