#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    digital_root.py                                             / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

"""
CodeWars exercise: codewars.com/users/peterbikes

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

"""

def digital_root(n):
    nr = str(n)
    res = 0
    i = 0
    while i < len(nr):
        res += int(nr[i])
        i+=1
    if(len(str(res)) > 1):
        res = digital_root(res)
    return res

print("Digital Root is the recursive sum of all digits in a number.")
number = input("Give me a posivite number: ")
print("The digital root of", number, "is", digital_root(int(number)))
