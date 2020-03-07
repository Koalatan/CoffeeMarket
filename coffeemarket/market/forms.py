from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, forms
from .models import InsertRegister


class Registration(ModelForm):
    class Meta:
        model = InsertRegister
        fields = ('name', 'user_id', 'password')
        labels = {
            'name': '名前',
            'user_id': 'ユーザーID',
            'password': 'パスワード',
        }


# ログインフォーム
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
