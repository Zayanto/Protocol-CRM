from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from properties.api.views import StageOpportunityAPIView, StageBuyingAPIView, StageTenantAPIView, StageRentAPIView

app_name='property-api'

urlpatterns = [
    path('properties/stage-opportunity/', StageOpportunityAPIView.as_view(), name='stage-opportunity'),
    path('properties/stage-buying/', StageBuyingAPIView.as_view(), name='stage-buying'),
    path('properties/stage-rent/', StageRentAPIView.as_view(), name='stage-rent'),
    path('properties/stage-tenant/', StageTenantAPIView.as_view(), name='stage-tenant'),
]
