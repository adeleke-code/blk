import sys, os
import csv
from django.conf import settings

from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

env_file = os.getenv('file_name')

base_dir = settings.BASE_DIR
csv_file_path = os.path.join(base_dir, env_file)





def extract_credentials():

    emails = []
    names = []

    with open(f"{csv_file_path}", 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            email = row[1]
            name = f"{row[2]} {row[3]}"
            
            emails.append(email)
            names.append(name)

    return emails, names


extracted_emails, extracted_names = extract_credentials()

for email, name in zip(extracted_emails, extracted_names):

    print(f"Email: {email}, Name: {name}")



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

    






def start_bulk():
    clear()
    print("""__________________________________________________________________________________________""")
    print("""__________________________________________________________________________________________""")
