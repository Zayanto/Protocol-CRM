from django.urls import path
from .views import *  # new
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),

    path('logout', views.logout, name='logout')
]
