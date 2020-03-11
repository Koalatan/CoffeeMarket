from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, forms
from .models import InsertRegister, CoffeeBeans


class Registration(ModelForm):
    class Meta:
        model = InsertRegister
        fields = ('name', 'user_id', 'password')
        labels = {
            'name': '名前',
            'user_id': 'ユーザーID',
            'password': 'パスワード',
        }


# 珈琲追加用form
class InsertBeans(ModelForm):
    class Meta:
        model = CoffeeBeans
        fields = ('beans_name', 'place', 'price', 'stock', 'beans_description')
        labels = {
            'beans_name': '豆名',
            'place': '採取地',
            'price': '値段',
            'stock': '在庫数',
            'beans_description': '商品説明'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['beans_name'].widget.attrs['class'] = 'form-control'
        self.fields['place'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['stock'].widget.attrs['class'] = 'form-control'
        self.fields['beans_description'].widget.attrs['class'] = 'form-control'
