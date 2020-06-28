from django.urls import path
from .views import ContractListView, ContractDetailView
from django.conf import settings

urlpatterns = [
    path('', ContractListView.as_view(), name='contract_list'),

    path('<uuid:pk>', ContractDetailView.as_view(),
         name='contract_detail'),

]
