from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  
from .models import Contract
from django.shortcuts import render



class ContractListView(LoginRequiredMixin, ListView):
    model = Contract
    context_object_name = 'contract_list'
    template_name = 'contracts/contract_list.html'
    login_url = 'account_login'


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Contract
    context_object_name = 'contract'
    template_name = 'contracts/contract_detail.html'
    login_url = 'account_login'
    permission_required = 'contracts.special_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = kwargs['object']
        # print(obj)
        photo_main = obj.reviews.all()
        context.update({
            'photo_main': photo_main,
        })
        # print(context)
        return context


