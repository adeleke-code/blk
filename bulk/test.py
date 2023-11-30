from .twillio import sms
import os, time, logging
from .models import MessagesSent
from twilio.rest import Client

from dotenv import find_dotenv, load_dotenv
import os, time

load_dotenv(find_dotenv())
from .helpers import *


account_sid = os.getenv('ssd_id')
auth_token = os.getenv('auth__')

client = Client(account_sid, auth_token)






def test():
    while True:
        
        print("""To exit, type 'exit',
                To test input correct phone number and press enter.
            """)

        res = input(":>>>>> ")
        if res == "":
            print("Please enter a valid command.")

        elif res == "exit":
            print("Exiting...")
            time.sleep(2)
            clear()
            sys.exit()

        if res != "" and res != "exit":
           
            try:
                res = client.messages.create(
                from_='Test Blk',
                body="Hi, This is a proxy test message.",
                to=res
                    )
                time.sleep(2)
                print(f"Message sent successfully to {res}")
                MessagesSent.objects.create(phone=res, status='sent')

                
            except Exception as e:
                logging.error("An error occurred: %s", str(e))
                print(f"Message not sent to {res}")
                print("Enter a valid phone number.")
                MessagesSent.objects.create(phone=res, status='failed')

                return