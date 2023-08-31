from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Coupon

@receiver(pre_save, sender=Coupon)
def check_coupon_expiration(sender, instance, **kwargs):
    if instance.expiration_date <= timezone.now():
        instance.active = False 
