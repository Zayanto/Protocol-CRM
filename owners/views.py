from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  
from .models import Owner



class OwnerListView(LoginRequiredMixin, ListView):
    model = Owner
    context_object_name = 'owner_list'
    template_name = 'owners/owner_list.html'
    login_url = 'account_login'


class OwnerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Owner
    context_object_name = 'owner'
    template_name = 'owners/owner_detail.html'
    login_url = 'account_login'
    permission_required = 'owners.special_status'



