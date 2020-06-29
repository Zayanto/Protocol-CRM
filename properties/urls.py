from django.urls import path
from .views import PropertyListView, PropertyDetailView, PropertyUpdateView, PropertyCreateView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', PropertyListView.as_view(), name='property_list'),

    path('<uuid:pk>', PropertyDetailView.as_view(),
         name='property_detail'),  # new

    path(
        '<uuid:pk>/update/',
        PropertyUpdateView.as_view(),
        name='property_update'
    ),

    path(
        'add/',
        PropertyCreateView.as_view(),
        name='add'
    ),
]
