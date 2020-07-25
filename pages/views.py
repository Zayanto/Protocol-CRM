from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from properties.models import Property
from tenants.models import Tenant
<<<<<<< HEAD
=======
from creating_user.models import *


>>>>>>> a22b3a0402bff5272c8be78954e841310a7a6efd


class HomePageView(TemplateView):
    template_name = 'home.html'
<<<<<<< HEAD
=======
    
    

>>>>>>> a22b3a0402bff5272c8be78954e841310a7a6efd

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'properties_count': Property.objects.count(),
            'tenants_count': Tenant.objects.count(),
<<<<<<< HEAD
=======
            
>>>>>>> a22b3a0402bff5272c8be78954e841310a7a6efd
        })
        # print(context)
        return context


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'
