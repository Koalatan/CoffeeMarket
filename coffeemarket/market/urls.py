from django.conf.urls import handler404
from django.contrib.auth.views import LoginView, LogoutView
from django.http import request
from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    # coffee関連
    path('newbeans/', views.InsertBeansView.as_view(), name='insertBeans'),
    path('newplace/', views.InsertPlaceView.as_view(), name='insertPlace'),
    path('top/', views.Top.as_view(), name='top'),
    path('bean/<int:pk>/', views.BeanDetail.as_view(), name='beanDetail'),

]