from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from properties.models import Property
from tenants.models import Tenant
from creating_user.models import *




class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'properties_count': Property.objects.count(),
            'tenants_count': Tenant.objects.count(),
        })
        # print(context)
        return context


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'
