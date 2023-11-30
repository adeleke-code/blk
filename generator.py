import csv
import random










"""DONT USE THIS FUNCTION"""

def generator(file_path, num_entries=600):

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['phone_number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_entries):

            phone_number = f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
            writer.writerow({'phone_number': phone_number})

    






# generator('config/ls.csv', num_entries=600)
