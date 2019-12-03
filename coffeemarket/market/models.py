from django.db import models


# Create your models here.


class InsertRegister(models.Model):
    userId = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

