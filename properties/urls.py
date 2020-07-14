from django.urls import path
from .views import PropertyListView, PropertyDetailView, PropertyUpdateView, PropertyCreateView, SearchResultsListView, PropertyImageUpload
from django.conf import settings
from django.conf.urls.static import static



app_name='property'

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

    path('search/', SearchResultsListView.as_view(), name='search_results'), # new


    path('image_upload/', PropertyImageUpload, name='image_upload'), # new
]
