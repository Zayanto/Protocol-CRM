from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # new
from .models import Property, PropertyImage
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect,HttpResponse


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
        property_images = obj.images.all()
        print(property_images)
        context.update({
            'tenants': tenants,
            'property_images': property_images,
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
        'description',
        'is_published',
        'list_date'
    ]
    action = "Update"


class SearchResultsListView(ListView):
    model = Property
    context_object_name = 'property_list'
    template_name = 'properties/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Property.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

def PropertyImageUpload(request):
    images = request.FILES.getlist('image_upload')
    property_id = request.POST.get('property_id')
    property_=Property.objects.get(id=property_id)
    if images:
        for image in images:
            PropertyImage.objects.create(image=image, _property=property_)
    return HttpResponse("ok")

