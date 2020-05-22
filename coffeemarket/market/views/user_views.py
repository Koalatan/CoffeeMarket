from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class UserInfoView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'user_info.html'
    login_url = '/accounts/login/'
