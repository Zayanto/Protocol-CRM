from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # new
from .models import Tenant


class TenantListView(LoginRequiredMixin, ListView):  # new
    model = Tenant
    context_object_name = 'tenant_list'
    template_name = 'tenants/tenant_list.html'
    login_url = 'account_login'  # new


class TenantDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # new
    model = Tenant
    context_object_name = 'tenant'
    template_name = 'tenants/tenant_detail.html'
    login_url = 'account_login'  # new
    permission_required = 'books.special_status'  # new
