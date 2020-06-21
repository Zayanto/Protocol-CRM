from django.urls import path
from .views import PropertyListView, PropertyDetailView

urlpatterns = [
    path('', PropertyListView.as_view(), name='property_list'),

    path('<uuid:pk>', PropertyDetailView.as_view(),
         name='property_detail'),  # new
]
