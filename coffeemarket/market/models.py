from django.db import models


# Create your models here.


class InsertRegister(models.Model):
    userId = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=25)


# コーヒー豆情報
class CoffeeBeans(models.Model):
    # id
    beansCode = models.CharField(max_length=5, primary_key=True)
    beansName = models.CharField(max_length=25)
    place = models.CharField(max_length=25)
    price = models.IntegerField(null=True, blank=True)
    # 登録日付 **更新日付はauto_now
    createDate = models.DateTimeField(auto_now_add=True)

