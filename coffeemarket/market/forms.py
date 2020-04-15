from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, forms
from .models import CoffeeBeans, PlaceCategory


# 珈琲追加用form
class InsertBeans(ModelForm):
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
class InsertPlace(ModelForm):
    class Meta:
        model = PlaceCategory
        fields = {'place'}
        labels = {
            'insert_place': '採取地'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place'].widget.attrs['place'] = 'form-control'