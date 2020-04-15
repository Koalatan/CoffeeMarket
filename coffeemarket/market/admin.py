from django.contrib import admin
from .models import PlaceCategory, CoffeeBeans, PaymentMethod,\
                    PurchaseDetail, PurchaseHistory
# Register your models here.

admin.site.register(PlaceCategory)
admin.site.register(CoffeeBeans)
admin.site.register(PaymentMethod)
admin.site.register(PurchaseDetail)
admin.site.register(PurchaseHistory)
