#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    hangman.py                                                  / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

import random
import os

def get_word():
    file = open('words.txt', 'r')
    number = random.randint(1, 10000)
    i = 0
    while i < number:
        word = file.readline()
        i += 1
    return word.removesuffix("\n")

def check_guessed(letters, word):
    for letter in word:
        if letter not in letters:
            return False
    return True

def hangman():
    word = get_word()
    guessed = False
    letters = [];
    tries = 15
    os.system("clear")
    while(True):
        guessed = check_guessed(letters, word);
        if(guessed):
            print("Word is", word.upper() + ", you won!")
            return;
        if(tries == 0):
            print("Word was", word.upper() + ", you LOST!!")
            return;
        print ("Hangman 💀")
        print("You have", tries, "tries left:")
        print("Letters tried:", letters)
        user_letter = input("Give us a letter please: ")
        os.system("clear")
        if(len(user_letter) == 1 and user_letter.isalpha()):
            letters.append(user_letter.lower())
        else:
            print("Stupid attempd, let's go ahead and deduct a try anyway.")
        for letter in word:
            if(letter in letters):
                print(letter.upper(), end=" ")
            else:
                print("_", end=" ")
        if(user_letter not in word):
            tries -= 1
        print("\n")


hangman()
