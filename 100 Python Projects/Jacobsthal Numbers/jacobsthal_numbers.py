#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    jacobsthal_numbers.py                                       / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #


def menu(choice, number):
    if(choice == '1'):
        print("Is", number, "part of Jacobsthal Sequence?", end=" ")
        print(bool(is_it_jacob(number)))
    if(choice == '2'):
        print("First Jacob after", number, "is", find_next_jacob(number))
    if(choice == '3'):
        print("First Jacob before", number, "is", find_prev_jacob(number))
    if(choice == '4'):
        print("All Jacobs till", number, ":", all_jacobs(number))

def is_it_jacob(number):
    if(number == 0 or number == 1):
        return True
    prev = 1
    i = 3
    swap = 0
    while i <= number:
        if(number == i):
            return True
        swap = i
        i = i + (2*prev)
        prev = swap
    return False

def find_next_jacob(number):
    if number == 0:
        return 1
    if number == 1:
        return 3
    prev = 1
    i = 3
    swap = 0
    while i <= number:
        swap = i
        i = i + (2*prev)
        prev = swap
    return i

def find_prev_jacob(number):
    if number == 0:
        return 0
    if number == 1:
        return 0
    prev = 1
    i = 3
    swap = 3
    while 1:
        if(i >= number):
            return prev
        swap = i
        i = i + (2*prev)
        prev = swap

def all_jacobs(number):
    lst = []
    while(number):
        if(is_it_jacob(number)):
            lst.append(number)
        number -=1
    lst.sort()
    return lst

print("In mathematics, the \033[1mJacobsthal\033[0m numbers are an integer sequence named after the German mathematician \033[1mErnst Jacobsthal.\033[0m")
print("In simple terms, the sequence starts with 0 and 1, then each following number is found by adding the number before it to twice the number before that. The first Jacobsthal numbers are:")
print("\033[1m0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, 87381, 174763, 349525, …\033[0m\n\n")
print("What would you like to do?")
print("1) find if number is part of Jacobsthal Sequence")
print("2) find next number part of Jacobsthal Sequence")
print("3) find previous number part of Jacobsthal Sequence")
print("4) find Jacobsthal Sequence numbers till number")

choice = input("Give us a choice: ")
while(choice != '1' and choice != '2' and choice != '3' and choice != '4'):
    choice = input("between 1 and 4: ")
number = input("Nice, now give us a number plz: ")
while(number.isdigit() == False):
    number = input("only digits, and keep them positive plz")

menu(choice, int(number))

