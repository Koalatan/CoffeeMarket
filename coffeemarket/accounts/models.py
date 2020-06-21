from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=8, blank=True)
    tel = models.CharField(max_length=12, blank=True)
