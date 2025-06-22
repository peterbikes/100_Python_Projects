#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    value_of_x.py                                               / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

def simple_calc(equation: str):
    op = '+'
    total = 0
    for num in equation:
        if num in '+-':
            op = num
        elif num.isdigit():
            if op == '+':
                total += int(num)
            elif op == '-':
                total -= int(num)
    return total


def is_x_negative(s):
    for i, char in enumerate(s):
        if char == 'x':
            # Check if index is at least 2 so we don't get IndexError
            if i >= 2 and s[i - 2] == '-':
                return -1
    return 1


def isolate_x(x_string, other_string):
    sideone = simple_calc(other_string.split())
    sidetwo = simple_calc(x_string.split())
    return sideone + (sidetwo*-1)


def solve(eq: str):
    is_neg = is_x_negative(eq)
    left, right = map(str.strip, eq.split('=', 1))
    if 'x' in left:
        return isolate_x(left, right)*is_neg
    else:
        return isolate_x(right, left)*is_neg
