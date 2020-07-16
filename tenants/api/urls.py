from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from tenants.api.views import CreateTenantAPIView

app_name = 'tenant-api'

urlpatterns = [
    path('properties/create-tenant/',
         CreateTenantAPIView.as_view(), name='create-tenant'),

]
