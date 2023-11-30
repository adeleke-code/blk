
import os
from twilio.rest import Client
import logging
from .models import MessagesSent
from dotenv import find_dotenv, load_dotenv
import os, time

load_dotenv(find_dotenv())


account_sid = os.getenv('ssd_id')
auth_token = os.getenv('auth__')

client = Client(account_sid, auth_token)






def sms(number):
    message = os.getenv('message')
    sender_name = os.getenv('sender_name')
    

    try:
        # res = client.messages.create(
        # from_=sender_name,
        # body=message,
        # to=number
        #     )
        time.sleep(2)
        print(f"Message sent successfully to {number}")
        MessagesSent.objects.create(phone=number, status='sent')

        
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        print(f"Message not sent to {number}")
        MessagesSent.objects.create(phone=number, status='failed')

        return


    return 
    
