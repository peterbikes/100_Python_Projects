#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    written_form.py                                             / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

tens =  {'9':'ninety',
         '8':'eighty',
         '7':'seventy',
         '6':'sixty',
         '5':'fifty',
         '4':'forty',
         '3':'thirty',
         '2':'twenty'}

teens =  {19:'nineteen',
          18:'eighteen',
          17:'seventeen',
          16:'sixteen',
          15:'fifteen',
          14:'fourteen',
          13:'thirteen',
          12:'twelve',
          11:'eleven',
          10:'ten',
          1:'one'}

singles =  {'9':'nine',
            '8':'eight',
            '7':'seven',
            '6':'six',
            '5':'five',
            '4':'four',
            '3':'three',
            '2':'two',
            '1':'one'}

def written_form(number):
    scent = ""
    if(number == 0):
        return("zero")
    if(len(str(number)) == 2 and str(number)[0] == '1'):
        return str(teens.get(number))
    if(len(str(number)) > 2):
        scent = scent + str(singles.get(str(number)[0]) + " hundred ")
        number %= 100
    if(str(number)[0] == '1'):
        return scent + str(teens.get(number))
    if(len(str(number)) > 1):
        scent = scent + str(tens.get(str(number)[0]) + " ")
        number %= 10
    if str(number) in singles:
        scent = scent + str(singles.get(str(number)))
    return scent

number = input("Give me a positive number up to 999: ")
while(len(number) > 3 or number.isdigit() == False):
    number = input("Wrong input, try again: ")

print(written_form(int(number)))
