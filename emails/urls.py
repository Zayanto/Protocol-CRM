
from django.urls import path
from .views import EmailListView, EmailDetailView
from django.conf import settings

urlpatterns = [
    path('', EmailListView.as_view(), name='email_list'),

    path('<uuid:pk>', EmailDetailView.as_view(),
         name='email_detail'),

]
