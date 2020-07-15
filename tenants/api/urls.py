from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from properties.api.views import CreateTenantAPIView

app_name='property-api'

urlpatterns = [
    path('properties/create-tenant/', CreateTenantAPIView.as_view(), name='create-tenant'),

]
