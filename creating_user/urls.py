from django.urls import path
from .views import *  # new
from . import views

urlpatterns = [
    path('page-users-edit',views.edit,name='edit'),
    path('page-users-list',views.list,name='list'),
    path('page-users-view/<str:pk>',views.view,name='view')
    
    

]
