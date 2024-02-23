#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    scramblies.py                                               / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

INSTRUCTIONS = "Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.\n\n"

print(INSTRUCTIONS)

def scramble(s1, s2):
    s1_list = list(s1)
    for char2 in s2:
        if char2 in s1_list:
            s1_list.remove(char2)
        else:
            return False
    return True


str1 = input("Give me string 1: ")
str2 = input("Give me string 2: ")

print("Can you write str2 with str1?")

if scramble(str1, str2):
	print("Yes you can :)")
else:
	print("No you can't :(")