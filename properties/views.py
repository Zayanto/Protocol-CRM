from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # new
from .models import Property
from django.shortcuts import render


class PropertyListView(LoginRequiredMixin, ListView):  # new
    model = Property
    context_object_name = 'property_list'
    template_name = 'properties/property_list.html'
    login_url = 'account_login'  # new

    def get(self, request, *args, **kwargs):
        total_properties = Property.objects.all().count()
        context = {'total_properties': total_properties}
        return render(request, self.template_name, context)


class PropertyDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # new
    model = Property
    context_object_name = 'property'
    template_name = 'properties/property_detail.html'
    login_url = 'account_login'  # new
    permission_required = 'properties.special_status'  # new
