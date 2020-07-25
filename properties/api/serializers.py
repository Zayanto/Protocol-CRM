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
<<<<<<< HEAD
    
class TenantMonthlyMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantMonthlyMaintenance
        fields = '__all__' 
=======
>>>>>>> a22b3a0402bff5272c8be78954e841310a7a6efd
    