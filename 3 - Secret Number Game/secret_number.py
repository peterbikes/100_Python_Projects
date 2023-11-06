#! /usr/bin/python

import random

secret_number = random.randint(1, 100)

user_number = input("Pick a number from 1 to 100: ")

while 1:
    if(int(user_number) < secret_number):
        user_number = input("Nope, think higher: ")
    if(int(user_number) > secret_number):
        user_number = input("Nope, think  lower: ")
    if(int(user_number) == secret_number):
        print("You won!")
        break

