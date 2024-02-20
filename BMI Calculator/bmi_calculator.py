#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    bmi_calculator.py                                           / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

height = input("Give me your height (cm): ")
weight = input("Give me your weight (kg): ")
try:
	print("Your BMI is", round(int(weight) / ((int(height) / 100) ** 2), 1))
except:
	print("Your values are incorrect somehow! Try again.")