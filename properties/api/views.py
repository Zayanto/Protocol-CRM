import datetime
import json
import time

from django.db.models import Q

from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.views import APIView

from properties.models import *
from properties.api.serializers import *
from contracts.models import *

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

class StageRenovationAPIView(APIView):
    serializer_class = StageRenovationSerializer
    
    def get(self, request):
        property_id = request.GET.get('property_id', None)

        if not property_id: 
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        stage_renovation, _ = StageRenovation.objects.get_or_create(properties=properties)
        serializer = self.serializer_class(stage_renovation, many=False)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        property_id = request.headers['property-id']
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj = StageRenovation.objects.get(properties=properties).delete()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    def post(self, request):
        property_id = request.POST.get('property_id', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)

        obj, _ = StageRenovation.objects.get_or_create(properties=properties)

        obj.investor = obj.investor if not request.POST.get('property-renovation-investor', None) else request.POST.get('property-renovation-investor', None)
        obj.renovation_budget = obj.renovation_budget if not request.POST.get('property-renovation-budget', None) else request.POST.get('property-renovation-budget', None)
        obj.date_receiving_money = obj.date_receiving_money if not request.POST.get('property-renovation-date-receiving-money', None) else datetime.strptime(request.POST.get('property-renovation-date-receiving-money'), '%Y-%m-%d')
        obj.date_receiving_key = obj.date_receiving_key if not request.POST.get('property-renovation-date-receiving-key', None) else datetime.strptime(request.POST.get('property-renovation-date-receiving-key'), '%Y-%m-%d')
        obj.description = obj.description if not request.POST.get('property-renovation-description', None) else request.POST.get('property-renovation-description', None)
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

class RenovationTeamCreateView(APIView):
    def post(self, request):
        property_id = request.POST.get('property_id', None)
        company_name = request.POST.get('company-name', None)
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')

        if not company_name:
            raise exceptions.NotFound('company_name is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        created = RenovationTeam.objects.create(renovation_stage=properties.stagerenovation, company_name=company_name)

        if created:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Error'}, status=status.HTTP_404_NOT_FOUND)

class RenovationTeamUpdateView(APIView):
    def post(self, request):
        property_id = request.POST.get('property_id', None)
        company_name = request.POST.get('company-name', None)
        renovation_team_id = request.POST.get('renovation-team-id', None)
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')

        if not company_name:
            raise exceptions.NotFound('company_name is not given')

        if not renovation_team_id:
            raise exceptions.NotFound('renovation_team_id is not given')
        
        try:
            properties = Property.objects.get(id=property_id)
            renovation_team = RenovationTeam.objects.get(id=renovation_team_id)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        renovation_team.company_name = company_name
        renovation_team.save()

        return Response({'status': 'success'}, status=status.HTTP_200_OK)

class MonthlyMaintenanceCreateView(APIView):
    def post(self, request):
        monthly_maintenance_model_id = request.POST.get('monthly_maintenance_model_id', None)
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        amount = request.POST.get('amount', None)
        currency = request.POST.get('currency', None)
        account = request.POST.get('account', None)
        date = request.POST.get('date', None)
        
        if not monthly_maintenance_model_id:
            raise exceptions.NotFound('monthly_maintenance_model_id is not given')

        if not title:
            raise exceptions.NotFound('title is not given')

        if not description:
            raise exceptions.NotFound('description is not given')

        if not amount:
            raise exceptions.NotFound('amount is not given')

        if not currency:
            raise exceptions.NotFound('currency is not given')

        if not account:
            raise exceptions.NotFound('account is not given')

        if not date:
            raise exceptions.NotFound('date is not given')

        try:
            monthly_maintenance_model = MonthlyMaintenanceModel.objects.get(id=monthly_maintenance_model_id)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        data = {
            'monthly_maintenance_model': monthly_maintenance_model,
            'title': title,
            'description': description,
            'amount': amount,
            'currency': currency,
            'account': account,
            'date': datetime.strptime(date, '%Y-%m-%d'),
        }
        try:
            created = MonthlyMaintenance.objects.create(**data)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        if created:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

class TenantMonthlyMaintenanceCreateView(APIView):
    def post(self, request):
        tenant_monthly_maintenance_model_id = request.POST.get('tenant_monthly_maintenance_model_id', None)
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        amount = request.POST.get('amount', None)
        currency = request.POST.get('currency', None)
        account = request.POST.get('account', None)
        date = request.POST.get('date', None)
        
        if not tenant_monthly_maintenance_model_id:
            raise exceptions.NotFound('tenant_monthly_maintenance_model_id is not given')

        if not title:
            raise exceptions.NotFound('title is not given')

        if not description:
            raise exceptions.NotFound('description is not given')

        if not amount:
            raise exceptions.NotFound('amount is not given')

        if not currency:
            raise exceptions.NotFound('currency is not given')

        if not account:
            raise exceptions.NotFound('account is not given')

        if not date:
            raise exceptions.NotFound('date is not given')

        try:
            tenant_monthly_maintenance_model = TenantMonthlyMaintenanceModel.objects.get(id=tenant_monthly_maintenance_model_id)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        data = {
            'tenant_monthly_maintenance_model': tenant_monthly_maintenance_model,
            'title': title,
            'description': description,
            'amount': amount,
            'currency': currency,
            'account': account,
            'date': datetime.strptime(date, '%Y-%m-%d'),
        }
        try:
            created = TenantMonthlyMaintenance.objects.create(**data)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        if created:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

class RenovationTeamExpenseCreateView(APIView):
    def post(self, request):
        expense_table_id = request.POST.get('expense_table_id', None)
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        amount = request.POST.get('amount', None)
        currency = request.POST.get('currency', None)
        account = request.POST.get('account', None)
        date = request.POST.get('date', None)
        store = request.POST.get('store', None)
        order_date = request.POST.get('order_date', None)
        delivery_date = request.POST.get('delivery_date', None)
        company = request.POST.get('company', None)
        
        if not expense_table_id:
            raise exceptions.NotFound('expense_table_id is not given')

        if not title:
            raise exceptions.NotFound('title is not given')

        if not description:
            raise exceptions.NotFound('description is not given')

        if not amount:
            raise exceptions.NotFound('amount is not given')

        if not currency:
            raise exceptions.NotFound('currency is not given')

        if not account:
            raise exceptions.NotFound('account is not given')

        if not date:
            raise exceptions.NotFound('date is not given')

        if not store:
            raise exceptions.NotFound('store is not given')

        if not order_date:
            raise exceptions.NotFound('order_date is not given')

        if not delivery_date:
            raise exceptions.NotFound('delivery_date is not given')

        if not company:
            raise exceptions.NotFound('company is not given')

        try:
            expense_table = ExpenseTable.objects.get(id=expense_table_id)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        data = {
            'expense_table': expense_table,
            'title': title,
            'description': description,
            'amount': amount,
            'currency': currency,
            'account': account,
            'date': datetime.strptime(date, '%Y-%m-%d'),
            'store': store,
            'order_date': datetime.strptime(order_date, '%Y-%m-%d'),
            'delivery_date': datetime.strptime(delivery_date, '%Y-%m-%d'),
            'company': company,
        }
        print(data)
        try:
            created = RenovationTeamExpenses.objects.create(**data)
        except Exception as e:
            raise exceptions.NotFound(e)
        
        if created:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

class ExpenseTableCreateView(APIView):
    def post(self, request):
        property_id = request.POST.get('property_id', None)
        renovation_team = request.POST.get('renovation-team', None)
        expense_table_name = request.POST.get('expense-table-name', None)
        
        if not property_id:
            raise exceptions.NotFound('property_id is not given')

        if not expense_table_name:
            raise exceptions.NotFound('expense_table_name is not given')

        if not renovation_team:
            raise exceptions.NotFound('Renovation Team id is not given')

        try:
            properties = Property.objects.get(id=property_id)
            renovation_team = RenovationTeam.objects.get(id=renovation_team)
        except Exception as e:
            raise exceptions.NotFound(e)

        created = ExpenseTable.objects.create(renovation_team=renovation_team, name=expense_table_name)

        if created:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

class AddContractInMonthlyExpense(APIView):
    def post(self, request):
        contract = request.POST.get('contract', None)
        
        if not contract:
            raise exceptions.NotFound('contract is not given')
        
        contract = Contract.objects.get(id=contract)
        contract.monthly_property_expense_track = True
        contract.save()
        
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

class CreateTenantMonthlyMaintenanceModel(APIView):
    def post(self, request):
        contract = request.POST.get('contract', None)
        name = request.POST.get('name', None)

        if not contract:
            raise exceptions.NotFound('contract is not given')

        if not name:
            raise exceptions.NotFound('name is not given')

        created = TenantMonthlyMaintenanceModel.objects.create(
            contract = Contract.objects.get(id=contract),
            name = name
        )

        if created:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

class CreateMonthlyMaintenanceModel(APIView):
    def post(self, request):
        property_id = request.POST.get('property_id', None)
        name = request.POST.get('name', None)

        if not property_id:
            raise exceptions.NotFound('property_id is not given')

        if not name:
            raise exceptions.NotFound('name is not given')

        created = MonthlyMaintenanceModel.objects.create(
            properties = Property.objects.get(id=property_id),
            name = name
        )

        if created:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)

class RenovationTeamListDatatableAPIView(ListAPIView):
    serializer_class = RenovationTeamSerializer

    def get_queryset(self):
        property_id = self.request.GET.get('property_id', None)
        if not property_id:
            raise exceptions.NotFound('Property id is not given')
        try:
            properties = Property.objects.get(id=property_id)
        except Exception as e:
            raise exceptions.NotFound(e)
        try:
            queryset = properties.stagerenovation.renovationteam_set.all().order_by('-created_date')
        except:
            queryset = RenovationTeam.objects.none()
        return queryset

    def get(self, request, *args, **kwargs):

        draw = request.GET.get('draw')
        qs = self.get_queryset()
        renovation_team_qs_range = qs

        draw = request.GET.get('draw')
        records_total = qs.count()
        records_filtered = qs.count()

        length = int(request.GET.get('length'))
        start = int(request.GET.get('start'))
        order_column = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]')
        search_str = request.GET.get('search[value]')

        page_num = int(request.GET.get('page_num', 1))

        column_names = [
            'company_name',
            'created_date',
            ''
        ]

        if search_str:
            renovation_team_qs_range = renovation_team_qs_range.filter(
                Q(company_name__icontains=search_str)
            )
            records_filtered = renovation_team_qs_range.count()

        if order_column:
            order_str = column_names[int(order_column)]

            if order_dir == 'desc':
                order_str = f'-{column_names[int(order_column)]}'

            renovation_team_qs_range = renovation_team_qs_range.order_by(order_str)
        # else:
        new_start = (page_num - 1) * length
        start = new_start if new_start <= records_filtered else start

        renovation_team_qs_range = renovation_team_qs_range[start:(start + length)]

        data_array = []

        for q in renovation_team_qs_range:
            
            data_array.append({
                'id': q.id,
                'company_name': q.company_name,
                'created_date': q.created_date.strftime("%b %d, %Y"),
            })

        response = {
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data_array
        }

        return Response(response, status=status.HTTP_200_OK)

class MonthlyMaintenanceDatatableAPIView(ListAPIView):
    serializer_class = MonthlyMaintenanceSerializer

    def get_queryset(self):
        monthly_maintenance_model_id = self.request.GET.get('monthly_maintenance_model_id', None)
        print(' <<<<sad')
        if not monthly_maintenance_model_id:
            raise exceptions.NotFound('monthly_maintenance_model_id is not given')
        
        queryset = MonthlyMaintenance.objects.filter(monthly_maintenance_model__id=monthly_maintenance_model_id).order_by('-created_date')
        return queryset

    def get(self, request, *args, **kwargs):

        draw = request.GET.get('draw')
        qs = self.get_queryset()
        monthly_maintenance_qs_range = qs

        draw = request.GET.get('draw')
        records_total = qs.count()
        records_filtered = qs.count()

        length = int(request.GET.get('length'))
        start = int(request.GET.get('start'))
        order_column = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]')
        search_str = request.GET.get('search[value]')

        page_num = int(request.GET.get('page_num', 1))

        column_names = [
            'title', 'description', 'amount', 'currency', 'account', 'date',
        ]

        if search_str:
            monthly_maintenance_qs_range = monthly_maintenance_qs_range.filter(
                Q(title__icontains=search_str) |
                Q(description__icontains=search_str) |
                Q(amount__icontains=search_str) |
                Q(currency__icontains=search_str) |
                Q(account__icontains=search_str)
            )
            records_filtered = monthly_maintenance_qs_range.count()

        if order_column:
            order_str = column_names[int(order_column)]

            if order_dir == 'desc':
                order_str = f'-{column_names[int(order_column)]}'

            monthly_maintenance_qs_range = monthly_maintenance_qs_range.order_by(order_str)
        # else:
        new_start = (page_num - 1) * length
        start = new_start if new_start <= records_filtered else start

        monthly_maintenance_qs_range = monthly_maintenance_qs_range[start:(start + length)]

        data_array = []

        for q in monthly_maintenance_qs_range:
            
            data_array.append({
                'id': q.id,
                'title': q.title,
                'description': q.description,
                'amount': q.amount,
                'currency': q.currency,
                'account': q.account,
                'date': q.date.strftime("%b %d, %Y"),
            })

        response = {
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data_array
        }

        return Response(response, status=status.HTTP_200_OK)
        

class TenantMonthlyMaintenanceDatatableAPIView(ListAPIView):
    serializer_class = TenantMonthlyMaintenanceSerializer

    def get_queryset(self):
        tenant_monthly_maintenance_model_id = self.request.GET.get('tenant_monthly_maintenance_model_id', None)

        if not tenant_monthly_maintenance_model_id:
            raise exceptions.NotFound('tenant_monthly_maintenance_model_id is not given')
        
        queryset = TenantMonthlyMaintenance.objects.filter(tenant_monthly_maintenance_model__id=tenant_monthly_maintenance_model_id).order_by('-created_date')
        return queryset

    def get(self, request, *args, **kwargs):

        draw = request.GET.get('draw')
        qs = self.get_queryset()
        tenant_monthly_maintenance_qs_range = qs

        draw = request.GET.get('draw')
        records_total = qs.count()
        records_filtered = qs.count()

        length = int(request.GET.get('length'))
        start = int(request.GET.get('start'))
        order_column = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]')
        search_str = request.GET.get('search[value]')

        page_num = int(request.GET.get('page_num', 1))

        column_names = [
            'title', 'description', 'amount', 'currency', 'account', 'date',
        ]

        if search_str:
            tenant_monthly_maintenance_qs_range = tenant_monthly_maintenance_qs_range.filter(
                Q(title__icontains=search_str) |
                Q(description__icontains=search_str) |
                Q(amount__icontains=search_str) |
                Q(currency__icontains=search_str) |
                Q(account__icontains=search_str)
            )
            records_filtered = tenant_monthly_maintenance_qs_range.count()

        if order_column:
            order_str = column_names[int(order_column)]

            if order_dir == 'desc':
                order_str = f'-{column_names[int(order_column)]}'

            tenant_monthly_maintenance_qs_range = tenant_monthly_maintenance_qs_range.order_by(order_str)
        # else:
        new_start = (page_num - 1) * length
        start = new_start if new_start <= records_filtered else start

        tenant_monthly_maintenance_qs_range = tenant_monthly_maintenance_qs_range[start:(start + length)]

        data_array = []

        for q in tenant_monthly_maintenance_qs_range:
            
            data_array.append({
                'id': q.id,
                'title': q.title,
                'description': q.description,
                'amount': q.amount,
                'currency': q.currency,
                'account': q.account,
                'date': q.date.strftime("%b %d, %Y"),
            })

        response = {
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data_array
        }

        return Response(response, status=status.HTTP_200_OK)
        
class RenovationTeamExpensesDatatableAPIView(ListAPIView):
    serializer_class = RenovationTeamExpensesSerializer

    def get_queryset(self):
        expense_table_id = self.request.GET.get('expense_table_id', None)
        
        if not expense_table_id:
            raise exceptions.NotFound('expense_table_id is not given')
        
        queryset = RenovationTeamExpenses.objects.filter(expense_table__id=expense_table_id).order_by('-created_date')
        return queryset

    def get(self, request, *args, **kwargs):

        draw = request.GET.get('draw')
        qs = self.get_queryset()
        renovation_team_expense_qs_range = qs

        draw = request.GET.get('draw')
        records_total = qs.count()
        records_filtered = qs.count()

        length = int(request.GET.get('length'))
        start = int(request.GET.get('start'))
        order_column = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]')
        search_str = request.GET.get('search[value]')

        page_num = int(request.GET.get('page_num', 1))

        column_names = [
            'title', 'description', 'amount', 'currency', 'account', 'date', 'store', 'order_date', 'delivery_date', 'company'
        ]

        if search_str:
            renovation_team_expense_qs_range = renovation_team_expense_qs_range.filter(
                Q(title__icontains=search_str) |
                Q(description__icontains=search_str) |
                Q(amount__icontains=search_str) |
                Q(currency__icontains=search_str) |
                Q(account__icontains=search_str) |
                Q(store__icontains=search_str) |
                Q(company__icontains=search_str)
            )
            records_filtered = renovation_team_expense_qs_range.count()

        if order_column:
            order_str = column_names[int(order_column)]

            if order_dir == 'desc':
                order_str = f'-{column_names[int(order_column)]}'

            renovation_team_expense_qs_range = renovation_team_expense_qs_range.order_by(order_str)
        # else:
        new_start = (page_num - 1) * length
        start = new_start if new_start <= records_filtered else start

        renovation_team_expense_qs_range = renovation_team_expense_qs_range[start:(start + length)]

        data_array = []

        for q in renovation_team_expense_qs_range:
            
            data_array.append({
                'id': q.id,
                'title': q.title,
                'description': q.description,
                'amount': q.amount,
                'currency': q.currency,
                'account': q.account,
                'date': q.date.strftime("%b %d, %Y"),
                'store': q.store,
                'order_date': q.order_date,
                'delivery_date': q.delivery_date,
                'company': q.company,
                'created_date': q.created_date.strftime("%b %d, %Y"),
            })

        response = {
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data_array
        }

        return Response(response, status=status.HTTP_200_OK)
