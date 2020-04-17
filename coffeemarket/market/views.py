from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.http import request
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views import generic, View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from .models import CoffeeBeans, PlaceCategory
from .forms import InsertBeans, InsertPlace


# Create your views here.
#
# def get_beans_data():
#     result = CoffeeBeans.objects.distinct('place')
#     result = list(result)
#     return result


# 珈琲豆追加view
# PermissionRequiredMixin アクセス制御 permission_required <app_name> <code_name>
class InsertBeansView(PermissionRequiredMixin, generic.CreateView):

    model = CoffeeBeans
    form_class = InsertBeans
    permission_required = ('market.can_add',)
    template_name = "coffeebeans_form.html"
    success_url = reverse_lazy('market:top')


# 地域登録 テンプレート側のnameをInsertPlaceのfield名と合わせる
class InsertPlaceView(View):

    def post(self, request):
        context = {}
        insert_place = InsertPlace(request.POST)
        # 登録
        if insert_place.is_valid():
            insert_place.save()

        return redirect("market:insertBeans")


# 珈琲豆一覧
class Top(generic.ListView):
    model = CoffeeBeans
    context_object_name = 'coffee_beans'
    template_name = 'top.html'


# (産地フィルター）珈琲豆一覧
class PlaceFilterBeanList(generic.ListView):

    model = CoffeeBeans
    context_object_name = 'coffee_beans'
    template_name = 'top.html'

    def get_queryset(self):
        place = self.kwargs['pk']
        return CoffeeBeans.objects.filter(place_category = place)


# 豆詳細
class BeanDetail(generic.DetailView):
    model = CoffeeBeans
    context_object_name = 'coffee_bean'
    template_name = 'coffeebean_detail.html'

# class InsertBeansView(TemplateView):
#
#     insert_bean_form = InsertBeans
#     insert_place_form = InsertPlace
#     template_name = 'coffeebeans_form.html'
#
#     def post(self, request):
#         bean_form = self.insert_bean_form(request.POST, request.FILES or None)
#         place_form = self.insert_place_form(request.POST, request.FILES or None)
#
#         if bean_form.is_valid():
#             self.bean_form.save()
#             print('豆成功')
#         elif place_form.is_valid():
#             self.place_form.save()
#             print('地域成功')
#         else:
#             context = {
#                 'error': '登録に失敗しました'
#             }
