#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    bit_counting.py                                             / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

def count_bits(n):
    binary_str = bin(n)
    count_ones = binary_str.count('1')
    return count_ones

number = input ("Give me a valid int: ")
print("Number of bits that are equal to one:", count_bits(int(number)))
