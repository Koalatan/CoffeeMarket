from django.conf.urls import handler404
from django.urls import path

from .views import Register
from . import views

app_name = 'market'

urlpatterns = [
    path('register/', views.Register.as_view(), name='create'),
    path('register/<ans>/', views.insertResult, name='insertResult'),
    path('top/', views.Top.as_view(), name='top'),
    path('account/login/', views.Login.as_view(), name='login'),
    path('account/logout/', views.Logout.as_view(), name='logout'),
]