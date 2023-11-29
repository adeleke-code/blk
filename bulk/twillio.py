
import os
from twilio.rest import Client
import logging
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())





account_sid = os.getenv('ssd_id')
auth_token = os.getenv('auth__')
client = Client(account_sid, auth_token)



def sms(number):
    message = os.getenv('message')
    sender_name = os.getenv('sender_name')
    

    try:
        res = client.messages.create(
        from_=sender_name,
        body=message,
        to=number
            )
        if res.status == "queued":
            print("Message sent successfully.")
    except Exception as e:

        logging.error("An error occurred: %s", str(e))
        return


    return res
    
