"""
user_name = input("Please Enter Name : >> ")
name_count = int(len(user_name))

while name_count < 1:
    print("Error. Please Try Again")
    user_name = input("Please Enter Name : >> ")

print("Result (2nd Char): ", user_name[1])
"""

import os

print("The Files and folders in {} are: ".format(os.getcwd()))
items = os.listdir(('.'))
for item in items:
    print(item)