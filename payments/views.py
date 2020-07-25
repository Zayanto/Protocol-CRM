from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  
from .models import Payment



class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    context_object_name = 'payment_list'
    template_name = 'payments/payment_list.html'
    login_url = 'account_login'


class PaymentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Payment
    context_object_name = 'payment'
    template_name = 'payments/payment_detail.html'
    login_url = 'account_login'
    permission_required = 'payments.special_status'



