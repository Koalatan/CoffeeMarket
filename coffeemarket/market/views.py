from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import InsertRegister
from .forms import Registration, LoginForm


# Create your views here.


class Register(generic.CreateView):
    # 一覧表示
    # モデル指定
    model = InsertRegister
    # form.pyのクラスを指定
    form_class = Registration
    template_name = "create_register.html"

    # 重複していない場合
    def form_valid(self, form):
        form.save()
        return redirect('market:insertResult', ans="good")

    # 重複している場合
    def form_invalid(self, form):
        return redirect('market:insertResult', ans="bad")


# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


# ログアウトページ
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


class Top(generic.TemplateView):
    template_name = 'top.html'


def insertResult(request, ans):
    context = {
        'message' : ans
    }
    return render(request, 'complete.html', context)





