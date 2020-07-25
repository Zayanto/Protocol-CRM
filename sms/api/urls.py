from django.urls import path
from django.conf import settings
from sms.api.views import SendWhatsappSMSAPIView

app_name = 'sms-api'

urlpatterns = [
    path('send-whatsapp-sms/', SendWhatsappSMSAPIView.as_view(), name='send-whatsapp-sms'),
]
