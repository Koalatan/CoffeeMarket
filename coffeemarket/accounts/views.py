from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.utils.functional import cached_property
from django.views import generic

from . import models
from .forms import LoginForm


# ログインページ


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


# ログアウトページ
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


# 会員情報閲覧用ページ
class UserInfo(LoginRequiredMixin, generic.TemplateView):
    template_name = 'user_info_detail.html'

    # cached_propertyをつけることにより
    # 2回目以降template側から呼び出した際に、
    # sqlが発行されずキャッシュから返すようになる
    @cached_property
    def userInfo(self):
        return models.Profile.objects.filter(user=self.request.user).first()
