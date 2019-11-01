from django.urls import path

from .views import Register
from . import views

app_name = 'market'

urlpatterns = [
    path('', Register.as_view(), name="create"),
    path('user/<ans>', views.insertResult, name="insertResult"),
]