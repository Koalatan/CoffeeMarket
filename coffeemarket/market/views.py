from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views import generic, View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from .models import CoffeeBeans, PlaceCategory, CartInfo, PurchaseHistory, PaymentMethod
from .forms import InsertBeans, InsertPlace, InsertCart, BeanVolume
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

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
        # aタグのpk取得・絞り込み
        place = self.kwargs['pk']
        return CoffeeBeans.objects.filter(place_category = place)


# 豆詳細　けん　カート追加処理
class BeanDetail(TemplateView):
    template_name = 'coffeebean_detail.html'
    # initialで

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        bean_id = self.kwargs['pk']
        coffee_beans = get_object_or_404(CoffeeBeans, id=bean_id)
        insert_cart = InsertCart
        context['coffee_bean'] = coffee_beans
        context['insert_cart'] = insert_cart
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        bean_id = self.kwargs['pk']
        user = self.request.user
        coffee_beans = get_object_or_404(CoffeeBeans, id=bean_id)
        volume = request.POST.get('volume')

        # method unique_exists() validate
        if CartInfo.check_unique_constrains(user, coffee_beans):
            context['msg'] = 'すでにカート内に登録されています。'

        else:
            context['msg'] = 'カートへの追加完了'
            cart_info = CartInfo(user=self.request.user, coffee_beans=coffee_beans, volume=volume)
            cart_info.save()

        return render(request, self.template_name, context)
        # CartInfo.objects.create(user=self.request.user, coffee_beans=coffee_beans, volume=volume)


# カート内情報閲覧
class CartInfoList(generic.TemplateView):
    template_name = 'cart_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        context['cart_info_list'] = CartInfo.objects.filter(user=user)
        context['public_key'] = settings.STRIPE_PUBLIC_KEY
        return context


# 購入処理
class BuyingProcessView(generic.TemplateView):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        cart_info_list = CartInfo.objects.filter(user=user)
        total_price = 0
        token = request.POST['stripeToken']
        # total_price calculation
        for cart_info in cart_info_list:
            total_price += cart_info.coffee_beans.price * cart_info.volume
        try:
            charge = stripe.Charge.create(
                amount=total_price,
                currency='jpy',
                source=token,
                description='珈琲豆売上'
            )
        except stripe.error.CardError as e:
            return redirect('market:buyingError')
        else:
            payment_method = get_object_or_404(PaymentMethod, pk=1)
            PurchaseHistory.objects.create(user_name=user,total_price=total_price,payment_code=payment_method)
            return redirect('market:buyingSuccess')


# 決済エラー
class BuyingErrorView(generic.TemplateView):
    template_name = 'buying_error.html'


# 決済完了
class BuyingSuccessView(generic.TemplateView):
    template_name = 'buying_success.html'

# # 豆詳細
# class BeanDetail(generic.DetailView):
#     model = CoffeeBeans
#     context_object_name = 'coffee_bean'
#     template_name = 'coffeebean_detail.html'


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
