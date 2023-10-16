import getpass
from datetime import date, datetime
import datetime
import csv
import pandas as pd

class Admission:
    def __init__(self,first_name,last_name):#,dob,email,gender,password2,course,contact):
        self.first_name = first_name
        self.last_name = last_name
        # self.dob       = dob
        # self.email      = email
        # self.gender     = gender
        # self.password2  = password2
        # self.course     = course
        # self.contact      = contact

    def signup(self):
        print("\n SILICON SIGN UP PAGE")
        # # FIRST NAME SETUP
        while True:
            #first_name = input("Enter your first name: ")
            try:
                self.first_name = input(" \n Enter your first name: ")
                first_name1 = self.first_name
                first_name1 = self.first_name.isalpha()
                if first_name1 == True:
        
                    #pass
                    print(self.first_name)
                    break

                else:
                    print("Please try again")
            except ValueError:
                print("Enter valid name")

        # # LAST NAME ENTRY
        while True:
            try:
                last_name = input("\n Enter your last name: ")
                last_name1 = last_name.isalpha()
                if last_name1 == True:
                
                    print(last_name)
                    break
                    #pass
                else:
                    print("Please try again")
            except ValueError:
                print("Enter valid name")

first_name = input(" \n Enter your first name: ") 
last_name = input("\n Enter your last name: ") 
admit = Admission()
#admit.signup()
print(f"charley it worked ooo {admit.first_name}, good job {admit.last_name}")