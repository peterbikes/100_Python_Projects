#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    caesar_cipher.py                                            / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

# idea taken from: codewars.com
# view my profile and solutions at: https://www.codewars.com/users/peterbikes

def moving_shift(s, shift):
    coded = ''
    for letter in s:
        flag = False;
        control = shift;
        if letter.isalpha():
            if(ord(letter) <= 90):
                while(flag == False):
                    if(ord(letter) + control > 90):
                        control -= 26     
                    else:        
                        coded += chr(ord(letter) + control)
                        flag = True
            else:
                while(flag == False):
                    if(ord(letter) + control > 122):
                            control -= 26     
                    else:
                        coded += chr(ord(letter) + control)
                        flag = True
        else:
            coded += letter
        shift += 1
    return coded;

def demoving_shift(s, shift):
    coded = ''
    for letter in s:
        flag = False;
        control = shift;
        if letter.isalpha():
            if(ord(letter) <= 90):
                while(flag == False):
                    if(ord(letter) - control < 65):
                        control -= 26    
                    else:    
                        coded += chr(ord(letter) - control)
                        flag = True
            else:
                while(flag == False):
                    if(ord(letter) - control < 97):
                            control -= 26    
                    else:
                        coded += chr(ord(letter) - control)
                        flag = True
        else:
            coded += letter
        shift += 1
    return coded;

choice = input('(C)ode or (D)ecode? ')
choice = choice.upper()
if(choice != 'C' and choice != 'D'):
    print("Invalid choice, goodbye! ")
    exit()

str = input('Sentence? ')
shift = input('Shifted how many times? (1 - 13): ')

if(shift.isdigit() == False or (int(shift) < 1 or int(shift) > 13)):
    print("Invalid choice, goodbye! ")
    exit() 

if (choice == 'C'):
    print(moving_shift(str, int(shift)))

if (choice == 'D'):
    print(demoving_shift(str, int(shift)))
