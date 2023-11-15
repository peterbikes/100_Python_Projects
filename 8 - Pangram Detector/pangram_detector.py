#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    pangram_detector.py                                         / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

# idea taken from: codewars.com
# view my profile and solutions at: https://www.codewars.com/users/peterbikes

def is_pangram(s):
    s = s.upper()
    for letter in "ABCDEFGHIJKLMNOPQRSTUVXYZ":
        if letter.isalpha() and (letter not in s):
            return False
    return True

s = input("Give me a sentence: ")


if (is_pangram(s) == True):
    print("Your sentece is a pangram")
if (is_pangram(s) == False):
    print("Your sentece is not a pangram")
