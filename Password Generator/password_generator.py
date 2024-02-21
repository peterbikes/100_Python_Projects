#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    password_generator.py                                       / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

import random
import string

NUMBERS = "1234567890"
SPECIALS = "~`!@#$%^&*()_+=-;:'?/><.,}{][|"

def return_number():
	choice = random.randint(0, 9)
	return NUMBERS[choice]

def return_special():
	choice = random.randint(0, 29)
	return SPECIALS[choice]

def password_generator(length, special, numbers, caps):
	password = ""
	regular = length -(special + numbers + caps)
	while(length):
		choice = random.randint(0, 3)
		if(choice == 0 and numbers > 0):
			password += return_number()
			numbers -= 1
			length -= 1
		if(choice == 1 and special > 0):
			password += return_special()
			special -= 1
			length -= 1
		if(choice == 2 and caps > 0):
			password += random.choice(string.ascii_uppercase)
			caps -= 1
			length -= 1
		if(choice == 3 and regular > 0):
			password += random.choice(string.ascii_lowercase)
			regular -= 1
			length -= 1
	return password

length = input("How long do you want this password to be? ")
special = 0
numbers = 0
caps = 0

while(length.isdigit() == False or int(length) > 100):
	length = input("Be reasonable - five me a valid int, lower than 100 chars please. ")

special = input("How many special chars? ")
while(special.isdigit() == False or int(special) > 100):
	special = input("Be reasonable - five me a valid int, lower than 100 chars please. ")

numbers = input("How many numbers? ")
while(numbers.isdigit() == False or int(numbers) > 100):
	numbers = input("Be reasonable - five me a valid int, lower than 100 chars please. ")

caps = input("How many caps? ")
while(caps.isdigit() == False or int(caps) > 100):
	caps = input("Be reasonable - five me a valid int, lower than 100 chars please. ")

if (int(special) + int(numbers) + int(caps) > int(length)):
	print("Ok, these numbers do not add up. Please run me again")
	exit()

print("Ok, here is your new password: ", end="")
print(password_generator(int(length), int(special), int(numbers), int(caps)))