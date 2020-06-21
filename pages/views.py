from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from properties.models import Property


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'
