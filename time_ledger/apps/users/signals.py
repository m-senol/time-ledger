from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .constants import LEAVE_DAYS

@receiver(post_save, sender=User)
def allocate_leave(sender, instance, created, **kwargs):
    if created:
        instance.available_leave_days = LEAVE_DAYS
        instance.save()
