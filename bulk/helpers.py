import sys, os
import csv
from django.conf import settings

from dotenv import find_dotenv, load_dotenv
import os, time
from .twillio import sms

load_dotenv(find_dotenv())

env_file = os.getenv('file_name')

base_dir = settings.BASE_DIR
csv_file_path = os.path.join(base_dir, env_file)





def extract():

    phone_numbers = []

    with open(f"{csv_file_path}", 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            phone = row[0]

            phone_numbers.append(phone)

    return phone_numbers



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




def start_bulk():
    clear()
    print("""__________________________________________________________________________________________""")
    extracted = extract()

    phone_list = extracted

    batch_size = 50
    batches = [phone_list[i:i + batch_size] for i in range(0, len(phone_list), batch_size)]

    

    for batch in batches:

        print(f"""Total number of phone numbers: {len(phone_list)}

        """)
        print(f"""Total number of batches: {len(batches)}

        """)

        print(f"Batch size: {len(batch)}")
        print(f"Batch: {batch}")
        
        print(f"Sending batch...")

        for phone in batch:
            sms(phone)

        print(f"Batch sent successfully...")
        print(f"Waiting for 10 minutes before sending next batch...")
        time.sleep(600)
        clear()



