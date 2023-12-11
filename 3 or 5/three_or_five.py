#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    three_or_five.py                                            / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

"""

CodeWars exercise: codewars.com/users/peterbikes

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

"""

def solution(number):
    result = 0
    if(number <= 0):
        return result
    number -= 1
    while(number):
        if(number % 3 == 0):
            result += number
            number -= 1
            continue
        if(number % 5 == 0):
            result += number
            number -= 1
            continue
        number -= 1
    return result;

number = input("Give me a positive number: ")
print(solution(int(number)))
