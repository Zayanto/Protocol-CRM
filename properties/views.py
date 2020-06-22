from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # new
from .models import Property
from django.shortcuts import render


class PropertyListView(LoginRequiredMixin, ListView):
    model = Property
    context_object_name = 'property_list'
    template_name = 'properties/property_list.html'
    login_url = 'account_login'


class PropertyDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Property
    context_object_name = 'property'
    template_name = 'properties/property_detail.html'
    login_url = 'account_login'
    permission_required = 'properties.special_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = kwargs['object']
        # print(obj)
        tenants = obj.reviews.all()
        context.update({
            'tenants': tenants,
        })
        # print(context)
        return context


class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    fields = [
        'title',
        'residence_complex',
        'state',
        'city',
        'address',
        'street_number',
        'zipcode',
        'building',
        'entrance',
        'apartament',
        'reper',
        'vecinatati',
        'destination',
        'layout',
        'floor',
        'comfort_type',
        'interior_state',
        'building_age',
        'usable_sqm',
        'build_sqm',
        'rooms',
        'bedrooms',
        'kitchen',
        'bathrooms',
        'balcony',
        'garage',
        'building_type',
        'construction_type',
        'basement',
        'notes',
        'lot_size',
        'buy_price',
        'sell_price',
        'rent',
        'photo_main',
        'photo_1',
        'photo_2',
        'photo_3',
        'photo_4',
        'photo_5',
        'photo_6',
        'photo_7',
        'photo_8',
        'photo_9',
        'photo_10',
        'photo_11',
        'photo_12',
        'description',
        'is_published',
        'list_date']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    fields = [
        'title',
        'residence_complex',
        'state',
        'city',
        'address',
        'street_number',
        'zipcode',
        'building',
        'entrance',
        'apartament',
        'reper',
        'vecinatati',
        'destination',
        'layout',
        'floor',
        'comfort_type',
        'interior_state',
        'building_age',
        'usable_sqm',
        'build_sqm',
        'rooms',
        'bedrooms',
        'kitchen',
        'bathrooms',
        'balcony',
        'garage',
        'building_type',
        'construction_type',
        'basement',
        'notes',
        'lot_size',
        'buy_price',
        'sell_price',
        'rent',
        'photo_main',
        'photo_1',
        'photo_2',
        'photo_3',
        'photo_4',
        'photo_5',
        'photo_6',
        'photo_7',
        'photo_8',
        'photo_9',
        'photo_10',
        'photo_11',
        'photo_12',
        'description',
        'is_published',
        'list_date'
    ]
    action = "Update"
