from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.views import APIView

from properties.models import *
from properties.api.serializers import StageOpportunitySerializer, StageBuyingSerializer, StageRentSerializer, StageTenantSerializer

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

    def post(self, request):
        property_id = request.POST.get('property_id', None)
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')

        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageOpportunity.objects.get_or_create(properties=property_id)
        obj.owner = obj.owner if not request.POST.get('owner', None) else obj.owner
        obj.asking_price = obj.asking_price if not request.POST.get('asking_price', None) else obj.asking_price
        obj.city = obj.city if not request.POST.get('city', None) else obj.city
        obj.residence_complex = obj.residence_complex if not request.POST.get('residence_complex', None) else obj.residence_complex
        obj.address = obj.address if not request.POST.get('address', None) else obj.address
        obj.zipcode = obj.zipcode if not request.POST.get('zipcode', None) else obj.zipcode
        obj.building = obj.building if not request.POST.get('building', None) else obj.building
        obj.entrance = obj.entrance if not request.POST.get('entrance', None) else obj.entrance
        obj.floor = obj.floor if not request.POST.get('floor', None) else obj.floor
        obj.apartament_number = obj.apartament_number if not request.POST.get('apartament_number', None) else obj.apartament_number
        obj.reper = obj.reper if not request.POST.get('reper', None) else obj.reper
        obj.vecinatati = obj.vecinatati if not request.POST.get('vecinatati', None) else obj.vecinatati
        obj.usable_sqm = obj.usable_sqm if not request.POST.get('usable_sqm', None) else obj.usable_sqm
        obj.build_sqm = obj.build_sqm if not request.POST.get('build_sqm', None) else obj.build_sqm
        obj.destination = obj.destination if not request.POST.get('destination', None) else obj.destination
        obj.layout = obj.layout if not request.POST.get('layout', None) else obj.layout
        obj.comfort_type = obj.comfort_type if not request.POST.get('comfort_type', None) else obj.comfort_type
        obj.interior_state = obj.interior_state if not request.POST.get('interior_state', None) else obj.interior_state
        obj.number_of_rooms = obj.number_of_rooms if not request.POST.get('number_of_rooms', None) else obj.number_of_rooms
        obj.bedrooms = obj.bedrooms if not request.POST.get('bedrooms', None) else obj.bedrooms
        obj.kitchen = obj.kitchen if not request.POST.get('kitchen', None) else obj.kitchen
        obj.bathrooms = obj.bathrooms if not request.POST.get('bathrooms', None) else obj.bathrooms
        obj.balcony = obj.balcony if not request.POST.get('balcony', None) else obj.balcony
        obj.garage = obj.garage if not request.POST.get('garage', None) else obj.garage
        obj.building_type = obj.building_type if not request.POST.get('building_type', None) else obj.building_type
        obj.building_construction_date = obj.building_construction_date if not request.POST.get('building_construction_date', None) else obj.building_construction_date
        obj.basement = obj.basement if not request.POST.get('basement', None) else obj.basement
        obj.potential_rent = obj.potential_rent if not request.POST.get('potential_rent', None) else obj.potential_rent
        obj.description = obj.description if not request.POST.get('description', None) else obj.description
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
    
    def post(self, request):
        property_id = request.POST.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageBuying.objects.get_or_create(properties=properties)
        obj.agent_costs = obj.agent_costs if not request.POST.get('agent_costs', None) else request.POST.get('agent_costs', None)
        obj.notary_costs = obj.notary_costs if not request.POST.get('notary_costs', None) else request.POST.get('notary_costs', None)
        obj.legal_costs = obj.legal_costs if not request.POST.get('legal_costs', None) else request.POST.get('legal_costs', None)
        obj.accountant_costs = obj.accountant_costs if not request.POST.get('accountant_costs', None) else request.POST.get('accountant_costs', None)
        obj.other_costs = obj.other_costs if not request.POST.get('other_costs', None) else request.POST.get('other_costs', None)
        obj.buy_price = obj.buy_price if not request.POST.get('buy_price', None) else request.POST.get('buy_price', None)
        obj.description = obj.description if not request.POST.get('description', None) else request.POST.get('description', None)
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
    
    def post(self, request):
        property_id = request.POST.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageForRent.objects.get_or_create(properties=properties)
        obj.expected_rent = obj.expected_rent if not request.POST.get('expected_rent', None) else request.POST.get('expected_rent', None)
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
    
    def post(self, request):
        property_id = request.POST.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageWithTenant.objects.get_or_create(properties=properties)
        obj.actual_rent = obj.actual_rent if not request.POST.get('actual_rent', None) else request.POST.get('actual_rent', None)
        obj.description = obj.description if not request.POST.get('description', None) else request.POST.get('description', None)
        obj.save()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    