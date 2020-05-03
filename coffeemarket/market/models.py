from django.db import models
from django.contrib.auth.models import User

# PlaceCategory
from django.db.models import UniqueConstraint


class PlaceCategory(models.Model):
    # id
    place = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.place


# CoffeeBeansInfo
class CoffeeBeans(models.Model):
    # id
    beans_name = models.CharField(max_length=25)
    price = models.IntegerField(null=True, blank=True)
    # 登録日付 **更新日付はauto_now
    create_date = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField()
    # 説明文
    beans_description = models.CharField(max_length=500, null=True, blank=True)
    # 外部キー制約
    place_category = models.ForeignKey(PlaceCategory, on_delete=models.CASCADE)

    # beans_image = models.ImageField(
    #     upload_to='market/',
    #     verbose_name='珈琲画像',
    # )


# now CartInfo
class CartInfo(models.Model):
    # id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee_beans = models.ForeignKey(CoffeeBeans, on_delete=models.CASCADE)
    volume = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'coffee_beans'], name='unique_cart')
        ]

    # ユニーク制約 validation用
    @classmethod
    def check_unique_constrains(cls, user: User, coffee_beans_pk: CoffeeBeans.pk) -> bool:
        return cls.objects.filter(user=user, coffee_beans_id=coffee_beans_pk).exists()


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
