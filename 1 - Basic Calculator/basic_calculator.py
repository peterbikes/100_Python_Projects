#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    basic_calculator.py                                         / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

print("This is a very basic calculator 🖩")

a = input("Give me the first number: ")
b = input("Give me the second number: ")
op = input("Chose an operation: + - * / ? ")

if op == '+':
    print(int(a) + int(b))
if op == '-':
    print(int(a) - int(b))
if op == '*':
    print(int(a) * int(b))
if op == '/':
    print(int(a) / int(b))

