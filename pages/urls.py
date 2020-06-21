from django.urls import path
from .views import AboutPageView, HomePageView  # new
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),  # new
]
