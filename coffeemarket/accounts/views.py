from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from .forms import LoginForm

# ログインページ


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


# ログアウトページ
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'