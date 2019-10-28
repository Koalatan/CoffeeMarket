from django.db import models

# Create your models here.


class InsertRegister(models.Model):

    name = models.CharField(max_length=50)
    userId = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
