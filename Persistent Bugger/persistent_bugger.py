#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    persistent_bugger.py                                        / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

"""
CodeWars exercise

check my profile at: codewars.com/users/peterbikes
-----

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

"""

def persistence(n):
    if len(str(n)) == 1:
        return 0
    result = 1;
    laps = 1
    while 1:
        for nr in str(n):
            result *= int(nr)
        if len(str(result)) == 1:
            return laps
        laps += 1
        n = result
        result = 1

print("Give me a number, and I will find out how many times you have to multiply its digits until you have a single one.")
print("For example: 39 --> 3, because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit.")

number = input("Your number please: ")

print(number, "persistent bugger is", persistence(number))
