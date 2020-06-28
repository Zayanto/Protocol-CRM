from django.urls import path
from .views import TenantListView, TenantDetailView

urlpatterns = [
    path('', TenantListView.as_view(), name='tenant_list'),
    path('<uuid:pk>', TenantDetailView.as_view(), name='tenant_detail'),  
]
