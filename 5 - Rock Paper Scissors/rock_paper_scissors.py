#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    rock_paper_scissors.py                                      / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

import random
import time

def lets_game(pc, player):
    print("🤜...rock...🤛", end="\r")
    time.sleep(1)
    print("🤜...paper...🤛", end="\r")
    time.sleep(1)
    print("🤜...scissors...🤛", end = "\n")
    time.sleep(1)
    if(pc == player):
        print("🪞 DRAW! 🪞")
    if(pc == 'R' and player == 'P'):
        print("🧻 PLAYER WON! 🪨")
    if(pc == 'R' and player == 'S'):
        print("✂️  COMPUTER WON :( 🪨")
    if(pc == 'P' and player == 'R'):
        print("🪨 COMPUTER WON :( 🧻")
    if(pc == 'P' and player == 'S'):
        print("✂️  PLAYER WON! 🧻")
    if(pc == 'S' and player == 'P'):
        print("🧻 COMPUTER WON :( ✂️")
    if(pc == 'S' and player == 'R'):
        print("🪨 PLAYER WON! ✂️")


pc_choice = random.randint(1, 3)
if(pc_choice == 1):
    pc_choice = 'R'
if(pc_choice == 2):
    pc_choice = 'P'
if(pc_choice == 3):
    pc_choice = 'S'

while 1:
    player = input("(R)ock, (P)aper, (S)cissors? ")
    player = player.capitalize()
    if(player != 'R' and player != 'P' and player != 'S'):
        print("invalid choice, try again")
    else:
        break

lets_game(pc_choice, player)
