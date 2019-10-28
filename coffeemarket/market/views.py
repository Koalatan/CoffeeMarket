from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import context
from django.views import generic
from .models import InsertRegister
from .forms import Registration

# Create your views here.


class Register(generic.CreateView):
    # モデル指定
    model = InsertRegister
    # form.pyのクラスを指定
    form_class = Registration
    template_name = "create_register.html"

    def form_valid(self, form):
        return render(request, 'complete.html', {
            'message': '認証に成功しました!'
        })

    def form_invalid(self, form):
        return render(request, 'bad.html', {
            'message': '認証に失敗しました！ \n 残念！'
        })



