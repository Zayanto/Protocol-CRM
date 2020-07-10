import datetime
import json

from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.views import APIView

from properties.models import *
from properties.api.serializers import StageOpportunitySerializer, StageBuyingSerializer, StageRentSerializer, StageTenantSerializer

class CreatePropertyStageOpportunityAPIView(APIView):

    def post(self, request):
        title = request.POST.get('property-title', None)

        if not title:
            return Response({'status': 'error', 'message': 'Please provide a title for the property!'}, status=status.HTTP_400_BAD_REQUEST)
        
        properties = Property.objects.create(title=title, description=request.POST.get('property-destination', ''))
    
        obj, _ = StageOpportunity.objects.get_or_create(properties=properties)
        obj.owner = obj.owner if not request.POST.get('property-owner', None) else request.POST.get('property-owner')
        obj.asking_price = obj.asking_price if not request.POST.get('property-asking-price', None) else request.POST.get('property-asking-price')
        obj.city = obj.city if not request.POST.get('property-city', None) else request.POST.get('property-city')
        obj.residence_complex = obj.residence_complex if not request.POST.get('property-residence-complex', None) else request.POST.get('property-residence-complex')
        obj.address = obj.address if not request.POST.get('property-address', None) else request.POST.get('property-address')
        obj.zipcode = obj.zipcode if not request.POST.get('property-zipcode', None) else request.POST.get('property-zipcode')
        obj.building = obj.building if not request.POST.get('property-building', None) else request.POST.get('property-building')
        obj.entrance = obj.entrance if not request.POST.get('property-entrance', None) else request.POST.get('property-entrance')
        obj.floor = obj.floor if not request.POST.get('property-floor', None) else request.POST.get('property-floor')
        obj.apartament_number = obj.apartament_number if not request.POST.get('property-apartament-number', None) else request.POST.get('property-apartament-number')
        obj.reper = obj.reper if not request.POST.get('property-reper', None) else request.POST.get('property-reper')
        obj.vecinatati = obj.vecinatati if not request.POST.get('property-vecinatati', None) else request.POST.get('property-vecinatati')
        obj.usable_sqm = obj.usable_sqm if not request.POST.get('property-usable_sqm', None) else request.POST.get('property-usable_sqm')
        obj.build_sqm = obj.build_sqm if not request.POST.get('property-build-sqm', None) else request.POST.get('property-build-sqm')
        obj.destination = obj.destination if not request.POST.get('property-destination', None) else request.POST.get('property-destination')
        obj.layout = obj.layout if not request.POST.get('property-layout', None) else request.POST.get('property-layout')
        obj.comfort_type = obj.comfort_type if not request.POST.get('property-comfort-type', None) else request.POST.get('property-comfort-type')
        obj.interior_state = obj.interior_state if not request.POST.get('property-interior-state', None) else request.POST.get('property-interior-state')
        obj.number_of_rooms = obj.number_of_rooms if not request.POST.get('property-number-of-rooms', None) else request.POST.get('property-number-of-rooms')
        obj.bedrooms = obj.bedrooms if not request.POST.get('property-bedrooms', None) else request.POST.get('property-bedrooms')
        obj.kitchen = obj.kitchen if not request.POST.get('property-kitchen', None) else request.POST.get('property-kitchen')
        obj.bathrooms = obj.bathrooms if not request.POST.get('property-bathrooms', None) else request.POST.get('property-bathrooms')
        obj.balcony = False if not request.POST.get('property-balcony', None) else True
        obj.garage = False if not request.POST.get('property-garage', None) else True
        obj.basement = False if not request.POST.get('property-basement', None) else True
        obj.building_type = obj.building_type if not request.POST.get('property-building-type', None) else request.POST.get('property-building-type')
        obj.building_construction_date = obj.building_construction_date if not request.POST.get('property-building-construction-date', None) else datetime.strptime(request.POST.get('property-building-construction-date'), '%Y-%m-%d')
        obj.potential_rent = obj.potential_rent if not request.POST.get('property-potential-rent', None) else request.POST.get('property-potential-rent')
        obj.description = obj.description if not request.POST.get('property-opportunity-description', None) else request.POST.get('property-opportunity-description')
        obj.save()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    

class StageOpportunityAPIView(APIView):
    serializer_class = StageOpportunitySerializer
    
    def get(self, request):
        property_id = request.GET.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')

        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        stage_opportunity, _ = StageOpportunity.objects.get_or_create(properties=properties)
        serializer = self.serializer_class(stage_opportunity, many=False)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        property_id = request.headers['property-id']
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj = StageOpportunity.objects.get(properties=properties).delete()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    def post(self, request):
        property_id = request.POST.get('property_id', None)
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageOpportunity.objects.get_or_create(properties=properties)
        obj.owner = obj.owner if not request.POST.get('property-owner', None) else request.POST.get('property-owner')
        obj.asking_price = obj.asking_price if not request.POST.get('property-asking-price', None) else request.POST.get('property-asking-price')
        obj.city = obj.city if not request.POST.get('property-city', None) else request.POST.get('property-city')
        obj.residence_complex = obj.residence_complex if not request.POST.get('property-residence-complex', None) else request.POST.get('property-residence-complex')
        obj.address = obj.address if not request.POST.get('property-address', None) else request.POST.get('property-address')
        obj.zipcode = obj.zipcode if not request.POST.get('property-zipcode', None) else request.POST.get('property-zipcode')
        obj.building = obj.building if not request.POST.get('property-building', None) else request.POST.get('property-building')
        obj.entrance = obj.entrance if not request.POST.get('property-entrance', None) else request.POST.get('property-entrance')
        obj.floor = obj.floor if not request.POST.get('property-floor', None) else request.POST.get('property-floor')
        obj.apartament_number = obj.apartament_number if not request.POST.get('property-apartament-number', None) else request.POST.get('property-apartament-number')
        obj.reper = obj.reper if not request.POST.get('property-reper', None) else request.POST.get('property-reper')
        obj.vecinatati = obj.vecinatati if not request.POST.get('property-vecinatati', None) else request.POST.get('property-vecinatati')
        obj.usable_sqm = obj.usable_sqm if not request.POST.get('property-usable_sqm', None) else request.POST.get('property-usable_sqm')
        obj.build_sqm = obj.build_sqm if not request.POST.get('property-build-sqm', None) else request.POST.get('property-build-sqm')
        obj.destination = obj.destination if not request.POST.get('property-destination', None) else request.POST.get('property-destination')
        obj.layout = obj.layout if not request.POST.get('property-layout', None) else request.POST.get('property-layout')
        obj.comfort_type = obj.comfort_type if not request.POST.get('property-comfort-type', None) else request.POST.get('property-comfort-type')
        obj.interior_state = obj.interior_state if not request.POST.get('property-interior-state', None) else request.POST.get('property-interior-state')
        obj.number_of_rooms = obj.number_of_rooms if not request.POST.get('property-number-of-rooms', None) else request.POST.get('property-number-of-rooms')
        obj.bedrooms = obj.bedrooms if not request.POST.get('property-bedrooms', None) else request.POST.get('property-bedrooms')
        obj.kitchen = obj.kitchen if not request.POST.get('property-kitchen', None) else request.POST.get('property-kitchen')
        obj.bathrooms = obj.bathrooms if not request.POST.get('property-bathrooms', None) else request.POST.get('property-bathrooms')
        obj.balcony = False if not request.POST.get('property-balcony', None) else True
        obj.garage = False if not request.POST.get('property-garage', None) else True
        obj.basement = False if not request.POST.get('property-basement', None) else True
        obj.building_type = obj.building_type if not request.POST.get('property-building-type', None) else request.POST.get('property-building-type')
        obj.building_construction_date = obj.building_construction_date if not request.POST.get('property-building-construction-date', None) else datetime.strptime(request.POST.get('property-building-construction-date'), '%Y-%m-%d')
        obj.potential_rent = obj.potential_rent if not request.POST.get('property-potential-rent', None) else request.POST.get('property-potential-rent')
        obj.description = obj.description if not request.POST.get('property-opportunity-description', None) else request.POST.get('property-opportunity-description')
        obj.save()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    

class StageBuyingAPIView(APIView):
    serializer_class = StageBuyingSerializer
    
    def get(self, request):
        property_id = request.GET.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        stage_buying, _ = StageBuying.objects.get_or_create(properties=properties)
        serializer = self.serializer_class(stage_buying, many=False)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        property_id = request.headers['property-id']
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj= StageBuying.objects.get(properties=properties).delete()
        
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    def post(self, request):
        property_id = request.POST.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageBuying.objects.get_or_create(properties=properties)
        obj.agent_costs = obj.agent_costs if not request.POST.get('property-agent-costs', None) else request.POST.get('property-agent-costs', None)
        obj.notary_costs = obj.notary_costs if not request.POST.get('property-notary-costs', None) else request.POST.get('property-notary-costs', None)
        obj.legal_costs = obj.legal_costs if not request.POST.get('property-legal-costs', None) else request.POST.get('property-legal-costs', None)
        obj.accountant_costs = obj.accountant_costs if not request.POST.get('property-accountant-costs', None) else request.POST.get('property-accountant-costs', None)
        obj.other_costs = obj.other_costs if not request.POST.get('property-other-costs', None) else request.POST.get('property-other-costs', None)
        obj.buy_price = obj.buy_price if not request.POST.get('property-buy-price', None) else request.POST.get('property-buy-price', None)
        obj.description = obj.description if not request.POST.get('property-buying-description', None) else request.POST.get('property-buying-description', None)

        obj.save()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)

class StageRentAPIView(APIView):
    serializer_class = StageRentSerializer
    
    def get(self, request):
        property_id = request.GET.get('property_id', None)

        if not property_id: 
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        stage_rent, _ = StageForRent.objects.get_or_create(properties=properties)
        serializer = self.serializer_class(stage_rent, many=False)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        property_id = request.headers['property-id']
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj = StageForRent.objects.get(properties=properties).delete()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    def post(self, request):
        property_id = request.POST.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageForRent.objects.get_or_create(properties=properties)
        obj.expected_rent = obj.expected_rent if not request.POST.get('property-expected-rent', None) else request.POST.get('property-expected-rent', None)
        obj.save()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    

class StageTenantAPIView(APIView):
    serializer_class = StageTenantSerializer
    
    def get(self, request):
        property_id = request.GET.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        stage_tenant, _ = StageWithTenant.objects.get_or_create(properties=properties)
        serializer = self.serializer_class(stage_tenant, many=False)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        property_id = request.headers['property-id']
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj = StageWithTenant.objects.get(properties=properties).delete()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
        
    def post(self, request):
        property_id = request.POST.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageWithTenant.objects.get_or_create(properties=properties)
        obj.actual_rent = obj.actual_rent if not request.POST.get('property-actual-rent', None) else request.POST.get('property-actual-rent', None)
        obj.description = obj.description if not request.POST.get('property-tenant-description', None) else request.POST.get('property-tenant-description', None)
        obj.save()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    