#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    remove_duplicates.py                                        / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

INSTRUCTIONS = "This one is simple - removes all characters that are unique from a string."

print(INSTRUCTIONS)

def count_chars(string, character):
	count = 0
	for c in string:
		if c == character:
			count += 1
	return count

def encode(string):
	coded = ""
	for char in string:
		if count_chars(string, char) > 1:
			coded += char
	return coded

string = input("\nPlease give me your phrase or word: ")

print("This is", string, "coded: ", encode(string))
