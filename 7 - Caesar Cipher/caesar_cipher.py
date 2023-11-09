#! /usr/bin/python

# idea taken from: codewars.com
# view my profile and solutions at: https://www.codewars.com/users/peterbikes

def moving_shift(s, shift):
    coded = ''
    for letter in s:
        if letter.isalpha():
            if(ord(letter) <= 90): #Capital letter
                if(ord(letter) + shift > 90):
                    coded += chr(ord(letter) + shift - 26)
                else:        
                    coded += chr(ord(letter) + shift)
            else:
                if(ord(letter) + shift > 122):
                    coded += chr(ord(letter) + shift - 26)
                else:
                    coded += chr(ord(letter) + shift)
        else:
            coded += letter
    return coded;

def demoving_shift(s, shift):
    coded = ''
    for letter in s:
        if letter.isalpha():
            if(ord(letter) <= 90): #Capital letter
                if(ord(letter) - shift < 65):
                    coded += chr(ord(letter) - shift + 26)
                else:        
                    coded += chr(ord(letter) - shift)
            else:
                if(ord(letter) - shift < 97):
                    coded += chr(ord(letter) - shift + 26)
                else:
                    coded += chr(ord(letter) - shift)
        else:
            coded += letter
    return coded;

choice = input('(C)ode or (D)ecode? ')
choice = choice.upper()
if(choice != 'C' and choice != 'D'):
    print("Invalid choice, goodbye! ")

str = input('Sentence? ')
shift = input('Shifted how many times? (1 - 13): ')

if(int(shift) < 1 or int(shift) > 13):
    print("Invalid choice, goodbye! ")

if (choice == 'C'):
    print(moving_shift(str, int(shift)))

if (choice == 'D'):
    print(demoving_shift(str, int(shift)))
