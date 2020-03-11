from django.conf.urls import handler404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    # coffee関連
    path('newbeans/', views.InsertBeansView.as_view(), name='insertBeans'),
    path('top/', views.Top.as_view(), name='top'),
    # path('top/<int:pk>/', )

]