#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    countdown_timer.py                                          / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

import time

seconds = input("How many seconds? ")

seconds = int(seconds)

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = "{:02d}:{:02d}".format(mins, secs)
    print("Time left:", timer, end="\r")
    time.sleep(1)
    seconds -= 1
print("Imagine an alarm is ringing instead of this line here")
