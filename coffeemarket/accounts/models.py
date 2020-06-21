from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=8, blank=True)
    tel = models.CharField(max_length=12, blank=True)


# シグナル@receiver 今回はUserに対してcreateが入力された時に実行される。
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# シグナル@receiver 今回はUserに対してsaveが入力された時に実行される。
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()