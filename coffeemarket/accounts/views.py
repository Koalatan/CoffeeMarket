from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.views import generic

from . import models
from .forms import LoginForm, ProfileForm


# ログインページ


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


# ログアウトページ
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


# 会員情報閲覧用ページ
class UserInfo(LoginRequiredMixin, generic.FormView):
    template_name = 'user_info_detail.html'
    form_class = ProfileForm
    success_url = reverse_lazy('accounts:userInfo')

    # cached_propertyをつけることにより
    # 2回目以降template側から呼び出した際に、
    # sqlが発行されずキャッシュから返すようになる
    @cached_property
    def userInfo(self):
        return models.Profile.objects.filter(user=self.request.user).first()

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        user_info = self.userInfo
        form.fields['address'].widget.attrs['placeholder'] = user_info.address
        form.fields['zip_code'].widget.attrs['placeholder'] = user_info.zip_code
        form.fields['tel'].widget.attrs['placeholder'] = user_info.tel
        return form

    def form_valid(self, form):
        user_info = self.userInfo
        user_info.address = form.data['address']
        user_info.zip_code = form.data['zip_code']
        user_info.tel = form.data['tel']
        user_info.save()
        return super().form_valid(form)
