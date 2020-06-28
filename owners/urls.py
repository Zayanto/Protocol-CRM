from django.urls import path
from .views import OwnerListView, OwnerDetailView
from django.conf import settings

urlpatterns = [
    path('', OwnerListView.as_view(), name='owner_list'),

    path('<uuid:pk>', OwnerDetailView.as_view(),
         name='owner_detail'),

]
