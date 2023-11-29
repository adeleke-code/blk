import json, os, sys, time
from django.core.management.base import BaseCommand, CommandError
from bulk.models import SenderDetails, MessagesSent
import logging
import psutil
from .helpers import *
import sys
from django.conf import settings
import os

from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

env_file = os.getenv('file_name')

base_dir = settings.BASE_DIR
csv_file_path = os.path.join(base_dir, env_file)


commands = """

Type Enter to continue...
Type 'exit' to exit...


"""

def main():

    while True:
        print("""
Click Enter to run analysis...
              
Type 'exit' to exit...
              
Type 'send' to start bulk sending sequence...

""")
        res = input(">>>>>> ")
        if res == "exit":
            print("""___________________EXITING_____________________
                  
                  """)
            time.sleep(2)
            clear()
            sys.exit()
            

        elif res == "":
            print("""..................TRYING TO ANALYZE CREDENTIALS..................
                  
                  """)


            time.sleep(3)
            if os.getenv('file_name') != None:
                print(f"""File name: {os.getenv('file_name')} was found. Analyzing file...
                      
                      """)
                
            else:
                print("""File name not found. Please set the file name in the .env file. 
                      
                      """)
                break
    

            time.sleep(3)
            try:
                if os.path.exists(f"{csv_file_path}") == True:
                    print("""File path exists. Analyzing file...
                          
                          """)
                else:
                    print("""File not found. Please check the file_name.
                          
                          """)
                    break
            except FileNotFoundError:
                print("""File not found. Please check the file_name.
                      
                      """)
                break

            time.sleep(3)
            if os.getenv('sender_name') != None and os.getenv('sender_name') != '':
                print(f"""Sender name: {os.getenv('sender_name')} was found.
                      
                      """)
            else:
                print("""Sender name not found. Please set the sender name in the .env file.
                      
                      """)
                break

            time.sleep(3)
            if os.getenv('message') != None and os.getenv('message') != '':
                print(f"""Message was found.
                      
                      """)
            else:
                print("Message not found. Please set the message in the .env file.")
                break

            print("""File analysis complete.
                  
                  """)
            time.sleep(5)
            clear()

        elif res == "send":
            print("""..................STARTING BULK SEQUENCE..................
                  
                  """)
            time.sleep(2)
            print("""Preparing Credentials...
                  
                  """)
            
            time.sleep(2)

            print(f"""<<<<<<<<<<<{os.getenv('sender_name').capitalize()}>>>>>>>>>>>
                  
                  
                  """)
            time.sleep(2)
            print(f"<<<<<<<<<{os.getenv('message').capitalize()}>>>>>>>>>>>")

            
            time.sleep(5)
           
        
        

        else:
            print("Invalid command. Please try again.")
            time.sleep(2)
            clear()
            main()
        
                











def collect_sender_details():
    while True:
        print("Enter Sender's Name:>>>")
        name = input()
        print("Enter Sender's Phone Number:>>>")
        phone = input()
        sender = SenderDetails.objects.create(name=name, phone=phone)
        print("Sender Details Saved.")
        break

