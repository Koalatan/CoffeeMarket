from django.forms import ModelForm, forms
from .models import InsertRegister


class Registration(ModelForm):
    class Meta:
        model = InsertRegister
        fields = ('name', 'userId', 'password')
        labels = {
            'name': '名前',
            'userId': 'ユーザーID',
            'password': 'パスワード',
        }
