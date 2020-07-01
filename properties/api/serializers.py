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
    
class StageRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageForRent
        fields = '__all__' 

class StageTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageWithTenant
        fields = '__all__' 
    