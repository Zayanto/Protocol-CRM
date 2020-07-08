
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  
from .models import Email



class EmailListView(LoginRequiredMixin, ListView):
    model = Email
    context_object_name = 'email_list'
    template_name = 'emails/email_list.html'
    login_url = 'account_login'


class EmailDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Email
    context_object_name = 'email'
    template_name = 'emails/email_detail.html'
    login_url = 'account_login'
    permission_required = 'emails.special_status'



