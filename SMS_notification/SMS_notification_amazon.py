from selenium import webdriver
from twilio.rest import Client
import os
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=os.getenv('TWILIO_PHONE'),
  body='ll',
  to=os.getenv('TWILIO_TO')

)


print(message.sid)