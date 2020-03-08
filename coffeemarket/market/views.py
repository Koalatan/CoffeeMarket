from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import InsertRegister, CoffeeBeans
from .forms import Registration, LoginForm, InsertBeans


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


# 珈琲豆追加view
class InsertBeansView(generic.CreateView):
    model = CoffeeBeans
    form_class = InsertBeans
    template_name = "coffeebeans_form.html"
    success_url = reverse_lazy('market:top')


# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


# ログアウトページ
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


class Top(generic.ListView):
    model = CoffeeBeans
    context_object_name = 'coffee_beans'
    template_name = 'top.html'


def insert_result(request, ans):
    context = {
        'message' : ans
    }
    return render(request, 'complete.html', context)





