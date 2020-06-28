from django.conf.urls import handler404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # ユーザ関連
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user/info/', views.UserInfo.as_view(), name='userInfo'),
]
