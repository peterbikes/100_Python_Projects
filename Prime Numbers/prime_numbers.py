#! /usr/bin/python

def menu(choice, number):
    if(choice == '1'):
        print("Is", number, "prime?", end=" ")
        print(bool(is_it_prime(number)))
    if(choice == '2'):
        print("First prime after", number, "is", find_next_prime(number))
    if(choice == '3'):
        print("First prime before", number, "is", find_prev_prime(number))
    if(choice == '4'):
        print("All primes till", number, ":", all_primes(number))

def is_it_prime(number):
    if(number == 0 or number == 1):
        return False
    i = 2
    while i < number:
        if(number % i == 0):
            return False
        i += 1
    return True

def find_next_prime(number):
    while 1:
        number += 1
        i = 2
        while(i <= number):
            if(number % i == 0):
                break
            if(i > number / 2):
                return number
            i += 1

def find_prev_prime(number):
    while number:
        number -= 1
        i = 2
        while(i <= number):
            if(number % i == 0):
                break
            if(i > number / 2):
                return number
            i += 1

def all_primes(number):
    lst = []
    while(number):
        if(is_it_prime(number)):
            lst.append(number)
        number -=1
    lst.sort()
    return lst

print("Welcome to prime time, what would you like to do?")
print("1) find if number is prime")
print("2) find next prime")
print("3) find previous prime")
print("4) find primes till number")
choice = input("Give us a choice: ")
while(choice != '1' and choice != '2' and choice != '3' and choice != '4'):
    choice = input("between 1 and 4: ")
number = input("Nice, now give us a number plz: ")
while(number.isdigit() == False):
    number = input("only digits, and keep them positive plz")

menu(choice, int(number))

