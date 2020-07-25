from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from django.contrib.auth import get_user_model

from tenants.models import *

User = get_user_model()

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__' 