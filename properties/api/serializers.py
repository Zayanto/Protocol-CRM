from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from django.contrib.auth import get_user_model

from properties.models import *

User = get_user_model()

class StageOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StageOpportunity
        fields = '__all__' 
    
class StageBuyingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageBuying
        fields = '__all__' 
    
class StageRenovationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageRenovation
        fields = '__all__' 
        
class StageRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageForRent
        fields = '__all__' 

class StageTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageWithTenant
        fields = '__all__' 

class RenovationTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenovationTeam
        fields = '__all__'

class RenovationTeamExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenovationTeamExpenses
        fields = '__all__' 
    

class MonthlyMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyMaintenance
        fields = '__all__' 
    
class TenantMonthlyMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantMonthlyMaintenance
        fields = '__all__' 
    