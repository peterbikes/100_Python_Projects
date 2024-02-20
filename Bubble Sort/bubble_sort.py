#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    bubble_sort.py                                              / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

# idea taken from: codewars.com
# view my profile and solutions at: https://www.codewars.com/users/peterbikes

def parse_lst(inp):
	if len(inp) < 2:
		print("You have to give me at least two numbers.")
		exit()
	lst = []
	for num in inp:
		if num.lstrip('-').isdigit():
			lst.append(int(num))
		else:
			print("Error found with input, use only int's please")
			exit()
	return lst

def bubble_sort(lst):
	i = 0
	temp = lst[0]
	while(i < len(lst) - 1):
		if(lst[i] > lst[i + 1]):
			temp = lst[i]
			lst[i] = lst[i + 1]
			lst[i + 1] = temp
			i = -1
		i += 1
	return lst

print("Give me a list of space separated numbers, like this:")
print("'1 2 3 5 4'")
inp = input("-> ")
print("Here is your sorted list: ", bubble_sort(parse_lst(inp.split())))