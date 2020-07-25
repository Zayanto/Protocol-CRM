import datetime
import json

from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.views import APIView

from tenants.models import *
from tenants.api.serializers import TenantSerializer

class CreateTenantAPIView(APIView):

    def post(self, request):
        full_name = request.POST.get('full_name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        description = request.POST.get('description', None)
        rent_tenant = request.POST.get('rent_tenant', None)
     

        if not full_name:
            return Response({'status': 'error', 'message': 'Please provide a name for the tenant!'}, status=status.HTTP_400_BAD_REQUEST)
            
        
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

