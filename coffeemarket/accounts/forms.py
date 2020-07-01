from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Profile


# ログインフォーム
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'zip_code', 'tel')
        labels = {
            'address': '住所',
            'zip_code': '郵便番号',
            'tel': '電話番号',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['zip_code'].widget.attrs['class'] = 'form-control'
        self.fields['tel'].widget.attrs['class'] = 'form-control'
