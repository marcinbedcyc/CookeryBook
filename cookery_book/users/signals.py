from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserAdditionalInfo


@receiver(post_save, sender=User)
def create_additionalinfo(sender, instance, created, **kwargs):
    if created:
        UserAdditionalInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_additionalinfo(sender, instance, **kwargs):
    instance.useradditionalinfo.save()
