from django.urls import path
from .views import PaymentListView, PaymentDetailView
from django.conf import settings

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment_list'),

    path('<uuid:pk>', PaymentDetailView.as_view(),
         name='payment_detail'),

]
