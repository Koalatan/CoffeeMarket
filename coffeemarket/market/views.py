from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import InsertRegister, CoffeeBeans
from .forms import Registration, InsertBeans


# Create your views here.


# 珈琲豆追加view
class InsertBeansView(generic.CreateView):
    model = CoffeeBeans
    form_class = InsertBeans
    template_name = "coffeebeans_form.html"
    success_url = reverse_lazy('market:top')


class Top(generic.ListView):
    model = CoffeeBeans
    context_object_name = 'coffee_beans'
    template_name = 'top.html'


class BeanDetail(generic.DetailView):
    model = CoffeeBeans
    context_object_name = 'coffee_beans'
    template_name = 'coffeebean_detail'



