from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('market:complete')
    # def form_valid(self, form):
    #     return render(request, 'complete.html', {
    #         'message': '認証に成功しました!'
    #     })

    # def form_invalid(self, form):
    #     return render(request, 'bad.html', {
    #         'message': '認証に失敗しました！ \n 残念！'
    #     })


def completeRegister(request):
    return render(request, 'complete.html', {'message': '登録完了!'})





