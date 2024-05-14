#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    petals.py                                                   / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

"""

CodeWars exercise: codewars.com/users/peterbikes

Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

"""

def lovefunc( flower1, flower2 ):
    if (flower1 + flower2) % 2 == 0:
        return False
    return True

print("Timmy and Sarah need to know if the sum of the number of petals on the flowers they hold are even or not.")
nr1 = input("How many petals does Sarah's flower have? ")
nr2 = input("What about Timmy's? ")

try:
    flower1 = int(nr1)
    flower2 = int(nr2)
except:
    print("Only ints please!! Try again.")
    exit()
if(lovefunc(flower1,flower2)):
    print("It's an odd number :(")
else:
    print("It's an even number :)")
