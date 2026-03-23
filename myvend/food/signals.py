from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from .models import FoodItem

@receiver(pre_save, sender=FoodItem)
def flag_expiring_items(sender, instance, **kwargs):
    instance.is_expiring_soon = instance.expiry_date <= timezone.now().date() + timedelta(days=7)