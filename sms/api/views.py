import json
import datetime
import re

from django.conf import settings
from django.contrib.auth import admin as auth_admin, get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.views import APIView
from rest_framework import exceptions, status

from twilio.rest import Client

User = get_user_model()

class SendWhatsappSMSAPIView(APIView):

    def get(self, request, *args, **kwargs):
        phonenumber = self.request.GET.get('phonenumber', '')
        message = self.request.GET.get('message', '')
        
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # this is the Twilio sandbox testing number
        from_whatsapp_number='whatsapp:+14155238886'
        
        to_whatsapp_number='whatsapp:+8801758558105'

        client.messages.create( body = message,
                                from_ = from_whatsapp_number,
                                to = to_whatsapp_number)
        response = {
            'status': 'success'
        }
        return Response(response, status=status.HTTP_200_OK)