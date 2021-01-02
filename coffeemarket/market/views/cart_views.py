# 豆詳細　けん　カート追加処理
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import TemplateView

from ..forms import InsertCart
from ..models import CoffeeBeans, CartInfo


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

    def post(self, *args, **kwargs):
        context = self.get_context_data()
        bean_id = self.kwargs['pk']
        user = self.request.user
        # coffee_beans = get_object_or_404(CoffeeBeans, id=bean_id)
        volume = self.request.POST.get('volume')

        # method unique_exists() validate
        if CartInfo.check_unique_constrains(user, bean_id):
            context['msg'] = 'すでにカート内に登録されています。'

        else:
            context['msg'] = 'カートへの追加完了'
            cart_info = CartInfo(user=user, coffee_beans_id=bean_id, volume=volume)
            cart_info.save()

        return render(self.request, self.template_name, context)
        # CartInfo.objects.create(user=self.request.user, coffee_beans=coffee_beans, volume=volume)


# カート内情報閲覧
class CartInfoList(LoginRequiredMixin, generic.TemplateView):
    template_name = 'cart_info.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        context['cart_info_list'] = CartInfo.objects.select_related('coffee_beans').filter(user=user)
        context['public_key'] = settings.STRIPE_PUBLIC_KEY
        return context
