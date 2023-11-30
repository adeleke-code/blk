from django.core.management.base import BaseCommand, CommandError
import json
from bulk.helpers import *
from bulk import main, test

import os
import sys, time


commands = """
To start session, type 'start'
To exit, type 'exit'

"""



class Command(BaseCommand):
    help = 'Start Session'


    def handle(self, *args, **options):
        while True:
            self.stdout.write(self.style.SUCCESS("TEST SESSION STARTED ... "))
            print (commands)
            response = input('>>>>>> ')
            if response == 'start':

                test.test()
            elif response == 'exit':
                self.stdout.write(self.style.SUCCESS("SESSION ENDED ... "))
                time.sleep(2)
                clear()
                sys.exit()

            else:
                self.stdout.write(self.style.SUCCESS("INVALID COMMAND ... "))
                time.sleep(2)
                clear()
            

       
          
        





