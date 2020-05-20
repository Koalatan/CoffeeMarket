from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views import generic, View

from ..forms import InsertBeans, InsertPlace
from ..models import CoffeeBeans, PlaceCategory, CartInfo, PurchaseHistory, PaymentMethod, PurchaseDetail


# 珈琲豆追加view
# PermissionRequiredMixin アクセス制御 permission_required <app_name> <code_name>
class InsertBeansView(PermissionRequiredMixin, generic.CreateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        message = self.request.GET.get('msg')
        if message is not None:
            context['msg'] = '入力された産地は既に追加されています。'
        return context

    model = CoffeeBeans
    form_class = InsertBeans
    permission_required = ('market.can_add',)
    template_name = "coffeebeans_form.html"
    success_url = reverse_lazy('market:top')


# 地域登録 テンプレート側のnameをInsertPlaceのfield名と合わせる
class InsertPlaceView(View):

    def post(self, *args, **kwargs):
        redirect_url = reverse('market:insertBeans')
        insert_place = InsertPlace(self.request.POST)
        # 登録

        if insert_place.is_valid():
            insert_place.save()
        else:
            query_string = urlencode({'msg': 'error'})
        redirect_url = '{}?{}'.format(redirect_url, query_string)
        return redirect(redirect_url)


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
        return CoffeeBeans.objects.filter(place_category=place)

