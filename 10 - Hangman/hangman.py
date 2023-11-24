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
    while(True):
        if(guessed):
            print("Word is", word.upper() + ", you won!")
            return;
        if(tries == 0):
            print("Word was", word.upper() + ", you LOST!!")
            return;
        os.system("clear")
        print ("Hangman 💀")
        print("You have", tries, "tries left:")
        print("Letters tried:", letters)
        for letter in word:
            if(letter in letters):
                print(letter.upper(), end=" ")
            else:
                print("_", end=" ")
        user_letter = input("\nGive us a letter please: ")
        while (len(user_letter) != 1 or user_letter.isalpha() == False):
            user_letter = input("Stupid attempd, try again: ")
        letters.append(user_letter.lower())
        if(user_letter not in word):
            tries -= 1
        guessed = check_guessed(letters, word);
        if(guessed == False and tries > 0):
            os.system("clear")

hangman()
