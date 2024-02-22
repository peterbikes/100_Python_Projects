#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    alphabet_symmetry.py                                        / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

INSTRUCTIONS = "Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word.\n\n"

print(INSTRUCTIONS)

def solve(strings : list[str]) -> list[int]:
	count = 0
	int_list = []
	i = 0
	for word in strings:
		while(i < len(word)):
			if(i - (ord(word[i].lower())) == -97):
				count += 1
			i += 1
		i = 0
		int_list.append(count)
		count = 0
	return int_list

size = input("How many words? ")

try:
	size = int(size)
	if size <= 0:
		exit()
except:
	print("ERROR: Valid positive ints please!!")
	exit()

size -= 1
words = [] 
string = input("Give me a word: ")
words.append(string)
while size:
	string = input("Another one please: ")
	words.append(string)
	size -= 1 

print("Here you go:", solve(words))

