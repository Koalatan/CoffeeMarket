from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class InsertRegister(models.Model):
    user_id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=25)


# CoffeeBeansInfo
class CoffeeBeans(models.Model):
    # id
    beans_name = models.CharField(max_length=25)
    place = models.CharField(max_length=25)
    price = models.IntegerField(null=True, blank=True)
    # 登録日付 **更新日付はauto_now
    create_date = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField()
    # 説明文
    beans_description = models.CharField(max_length=500, null=True, blank=True)

# PaymentStyle
class PaymentMethod(models.Model):
    # id
    payment_method = models.CharField(max_length=25)


# CustomerPurchaseHistry
class PurchaseHistory(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(null=True, blank=True)
    payment_code = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    buy_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id', 'user_name')


# CustomerPurchaseDetail !!! Django Compound primary key not supported!!
class PurchaseDetail(models.Model):
    purchase_code = models.ForeignKey(PurchaseHistory, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    detail_code = models.CharField(max_length=5)
    beans_code = models.ForeignKey(CoffeeBeans, on_delete=models.CASCADE)
    selling_price = models.IntegerField()

    # multi-unique-setting
    class Meta:
        unique_together = ('purchase_code', 'user_name', 'detail_code')


