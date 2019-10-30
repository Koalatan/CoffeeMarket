from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import InsertRegister
from .forms import Registration

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
        return redirect('market:insertResult')

    # 重複している場合
    def form_invalid(self, form):
        print('重複')
        return redirect('market:insertResult')


def insertResult(request):
    return render(request, 'complete.html')





