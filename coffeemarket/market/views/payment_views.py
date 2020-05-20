import stripe
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.views import generic

from ..models import PurchaseDetail, CartInfo, PurchaseHistory


# 購入処理
def savePurchaseDetail(purchase_history_pk, cart_info_list):
    for cart_info in cart_info_list:
        PurchaseDetail.objects.create(
            purchase_code_id=purchase_history_pk, beans_code_id=cart_info.coffee_beans.pk,
            selling_price=cart_info.coffee_beans.price, volume=cart_info.volume
        )


def sumTotalPrice(cart_info_list):
    total_price = 0
    for cart_info in cart_info_list:
        total_price += cart_info.coffee_beans.price * cart_info.volume
    return total_price


class BuyingProcessView(generic.TemplateView):

    def post(self, *args, **kwargs):
        user = self.request.user
        cart_info_list = CartInfo.objects.filter(user=user)
        token = self.request.POST['stripeToken']
        # total_price calculation
        total_price = sumTotalPrice(cart_info_list)
        try:
            charge = stripe.Charge.create(
                amount=total_price,
                currency='jpy',
                source=token,
                description='珈琲豆売上',
                api_key=settings.STRIPE_SECRET_KEY
            )
        except stripe.error.CardError as e:
            return redirect('market:buyingError')
        except Exception as e:
            # 重大なエラー (APIの仕様変更等,　エラーの範囲が広すぎるかも。
            return redirect('market:buyingError')

        else:
            # 購入履歴に保存
            buy_date = timezone.now()
            PurchaseHistory.objects.create(
                user_name=user, total_price=total_price, payment_code_id=1, buy_date=buy_date
            )
            purchase_history_pk = \
                PurchaseHistory.objects.filter(user_name=user, buy_date=buy_date).values_list('id', flat=True)

            if len(purchase_history_pk) != 1:
                print(purchase_history_pk)
                print("err!")
            else:
                savePurchaseDetail(purchase_history_pk[0], cart_info_list)
            return redirect('market:buyingSuccess')


class PurchaseView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'purchase_historys'
    template_name = 'purchase_history.html'

    def get_queryset(self):
        user = self.request.user
        query_set = PurchaseHistory.objects.filter(user_name=user)
        return query_set


class PurchaseHistoryDetailView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'purchase_details'
    template_name = 'purchase_detail.html'

    def get_queryset(self):
        user = self.request.user
        purchase_id = self.kwargs['pk']
        query_set = PurchaseDetail.objects.filter(
            purchase_code_id=purchase_id, purchase_code__user_name=user
        )
        # select_related('beans_code', 'purchase_code', 'purchase_code__user_name').\
        # get(purchase_code=purchase_id, id=user.pk)

        return query_set


# 決済エラー
class BuyingErrorView(generic.TemplateView):
    template_name = 'buying_error.html'


# 決済完了
class BuyingSuccessView(generic.TemplateView):
    template_name = 'buying_success.html'
