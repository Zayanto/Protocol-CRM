from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
TWILIO_ACCOUNT_SID='AC6c42431e52233421a2c7083c57781ec5'
TWILIO_AUTH_TOKEN='1cea2c50661a7337d8091877e07549c4'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+8801758558105'

client.messages.create( body = 'Hello world!',
                        from_ = from_whatsapp_number,
                        to = to_whatsapp_number)