#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    par_encoder.py                                              / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

INSTRUCTIONS = "The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate. Capitalization is ignored."

print(INSTRUCTIONS)

def count_chars(string, character):
	count = 0
	for c in string:
		if c.lower() == character.lower():
			count += 1
	return count

def encode(string):
	coded = ""
	for char in string:
		if count_chars(string, char) == 1:
			coded += '('
		else:
			coded += ')'
	return coded

string = input("\nPlease give me your phrase or word: ")

print("This is", string, "coded: ", encode(string))
