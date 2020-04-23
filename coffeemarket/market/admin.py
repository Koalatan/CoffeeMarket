from django.contrib import admin
from .models import PlaceCategory, CoffeeBeans, PaymentMethod, \
    PurchaseDetail, PurchaseHistory, CartInfo

# Register your models here.

admin.site.register(PlaceCategory)
admin.site.register(CartInfo)
admin.site.register(CoffeeBeans)
admin.site.register(PaymentMethod)
admin.site.register(PurchaseDetail)
admin.site.register(PurchaseHistory)
