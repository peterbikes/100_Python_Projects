#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    rgb_to_hex.py                                               / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

def rgb(r, g, b):
	rgb = ""
	rgb += hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)
	return rgb.upper()

r = input("Give me your R value: ")
g = input("Give me your B value: ")
b = input("Give me your G value: ")

try:
	print("Value in RGB form: ", rgb(int(r), int(g), int(b)))
except:
	print("Invalid values given, try again.")