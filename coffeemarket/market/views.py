from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.model import CreateRegister

# Create your views here.


class Register(generic.CreateView):
    # モデル指定
    model = CreateRegister
    # form.pyのクラスを指定
    form_class = Registration
    template_name = "create_register.html"
    success_url = reverse_lazy('complete')

