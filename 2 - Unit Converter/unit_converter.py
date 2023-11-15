#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    unit_converter.py                                           / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

def mile_km(num):
    return(num*1.609344)

def km_mile(num):
    return(num*0.6213712)

def foot_meter(num):
    return(num*0.3048)

def meter_foot(num):
    return(num*3.28084)

def celsius_fahr(num):
    return((num*1.8)+32)

def fahr_celsius(num):
    return(round(((num - 32) *(5/9)), 2))

def kilo_pound(num):
    return(num * 2.2)

def pound_kilo(num):
    return(round((num / 2.2), 2))

print("Unit Converter\n")

choice = input("What kind of conversion would you like?\n1) Mile | Kilometer\n2) Foot | Meter\n3) Celsius | Fahrenheit\n4) Kilogram | Pound ")

if (int(choice) != 1 and int(choice) != 2 and int(choice) != 3 and int(choice) != 4):
    print("Invalid choice, goodbye :)")

if(choice == '1'):
    choice = input(("\n1) Mile to Kilometer\n2) Kilometer to Mile\n"))
    if (choice != '1' and choice != '2'):
        print("Invalid choice, goodbye :)")
    elif choice == '1':
        num = input("How many? ")
        print(num, " miles are ", mile_km(int(num)), "km.")
        exit()
    elif choice == '2':
        num = input("How many? ") 
        print(num, " kilometers are ", km_mile(int(num)), " miles.")
        exit()

if(choice == '2'):
    choice = input(("\n1) Foot to Meter\n2) Meter to Foot\n"))
    if (choice != '1' and choice != '2'):
        print("Invalid choice, goodbye :)")
    elif choice == '1':
        num = input("How many? ")
        print(num, "foot are", foot_meter(int(num)), "meter.")
        exit()
    elif choice == '2':
        num = input("How many? ") 
        print(num, "meters are", meter_foot(int(num)), "foot.")
        exit()

if(choice == '3'):
    choice = input(("\n1) Celsius to Fahrenheit\n2) Fahrenheit to Celsius\n"))
    if (choice != '1' and choice != '2'):
        print("Invalid choice, goodbye :)")
    elif choice == '1':
        num = input("How many? ")
        print(num, "degrees celsius are", celsius_fahr(int(num)), "degrees fahrenheit.")
        exit()
    elif choice == '2':
        num = input("How many? ") 
        print(num, "degrees fahrenheit are", fahr_celsius(int(num)), "degrees celsius.")
        exit()

if(choice == '4'):
    choice = input(("\n1) Pounds to Kilos\n2) Kilos to Pounds\n"))
    if (choice != '1' and choice != '2'):
        print("Invalid choice, goodbye :)")
    elif choice == '1':
        num = input("How many? ")
        print(num, "Pounds are", pound_kilo(int(num)), "Kilos.")
        exit()
    elif choice == '2':
        num = input("How many? ") 
        print(num, "Kilos", kilo_pound(int(num)), "Pounds.")
        exit()
