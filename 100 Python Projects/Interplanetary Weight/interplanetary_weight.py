#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    interplanetary_weight.py                                    / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

BOLD = "\033[1m"
YELLOW = "\033[93m"
LIGHT_BROWN = "\033[38;2;205;133;63m"
BABY_BLUE = "\033[38;2;173;216;230m"
GREEN = "\033[32m"
BLOOD_RED = "\033[38;2;139;0;0m"
BROWN = "\033[38;2;165;42;42m"
PURPLE = "\033[38;2;128;0;128m"
GREY = "\033[38;2;128;128;128m"
SEA_BLUE = "\033[38;2;0;105;148m"
RESET = "\033[0m"

print("Welcome to Interplanetary Weight 🪐\n")

weight_inp = input("Give me your weight in KG: ")

try:
	weight = float(weight_inp)
except ValueError:
	print("Error in input! please enter a valid number.")
	exit()

try:
	print(BOLD + YELLOW + "\nSUN     : " + RESET + BOLD + str(round(weight * 27)) + " KG")
	print(LIGHT_BROWN + "MERCURY : " + RESET + BOLD + str(round(weight * 3.7)) + " KG")
	print(BABY_BLUE + "VENUS   : " + RESET + BOLD + str(round(weight * 8.87)) + " KG")
	print(GREEN + "EARTH   : " + RESET + BOLD + str(round(weight)) + " KG")
	print(BLOOD_RED + "MARS    : " + RESET + BOLD + str(round(weight * 3.7)) + " KG")
	print(BROWN + "JUPITER : " + RESET + BOLD + str(round(weight * 24.79)) + " KG")
	print(PURPLE + "SATURN  : " + RESET + BOLD + str(round(weight * 10.44)) + " KG")
	print(GREY + "URANUS  : " + RESET + BOLD + str(round(weight * 8.69)) + " KG")
	print(SEA_BLUE + "NEPTUN  : " + RESET + BOLD + str(round(weight * 11.15)) + " KG")
	print(RESET + "(... and, controversial)\n" + BOLD + "PLUTO   : " + str(round(weight * 0.62)) + " KG")


except:
	print("Error in input! Try again.")