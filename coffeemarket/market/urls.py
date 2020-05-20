from django.conf.urls import handler404
from django.contrib.auth.views import LoginView, LogoutView
from django.http import request
from django.urls import path
from .views import bean_views, cart_views, payment_views

app_name = 'market'

urlpatterns = [
    # coffee関連
    path('newbeans/', bean_views.InsertBeansView.as_view(), name='insertBeans'),
    path('newplace/', bean_views.InsertPlaceView.as_view(), name='insertPlace'),
    path('bean/list/', bean_views.Top.as_view(), name='top'),
    path('bean/<int:pk>/', cart_views.BeanDetail.as_view(), name='beanDetail'),
    path('bean/list/filter/<int:pk>/', bean_views.PlaceFilterBeanList.as_view(), name='filterBeanList'),
    path('user/cart/', cart_views.CartInfoList.as_view(), name='cartInfo'),
    path('user/cart/buying/', payment_views.BuyingProcessView.as_view(), name='buyingProcess'),
    path('user/cart/buying/error/', payment_views.BuyingErrorView.as_view(), name='buyingError'),
    path('user/cart/buying/success/', payment_views.BuyingSuccessView.as_view(), name='buyingSuccess'),
    path('user/cart/history/', payment_views.PurchaseView.as_view(), name='purchaseHistory'),
    path('user/cart/history/<int:pk>', payment_views.PurchaseHistoryDetailView.as_view(), name='purchaseHistoryDetail'),
    # path('cart/', views.InsertCartView.as_view(), name='insertCart'),
]