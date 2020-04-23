from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CoffeeBeans, PlaceCategory, CartInfo


# 珈琲追加用form
class InsertBeans(forms.ModelForm):
    class Meta:
        model = CoffeeBeans
        fields = ('beans_name', 'place_category', 'price', 'stock', 'beans_description')
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
        self.fields['place_category'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['stock'].widget.attrs['class'] = 'form-control'
        self.fields['beans_description'].widget.attrs['class'] = 'form-control'


# 産地登録用form
class InsertPlace(forms.ModelForm):
    class Meta:
        model = PlaceCategory
        fields = {'place'}
        labels = {
            'insert_place': '採取地'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place'].widget.attrs['class'] = 'form-control'


class InsertCart(forms.ModelForm):
    class Meta:
        model = CartInfo
        fields = ('user', 'coffee_beans', 'volume')
        labels = {
            'user': 'user',
            'coffee_beans': 'id',
            'volume': '数量',
        }
        widgets = {
            'user': forms.HiddenInput(),
            'coffee_beans': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['volume'].widget.attrs['class'] = 'form-control'


class BeanVolume(forms.Form):

    volume = forms.IntegerField(
        label='数量',
        max_value=5,
        min_value=1
    )