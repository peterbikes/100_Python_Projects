# **************************************************************************** #
#                                                                 __           #
#    podp.py                                                     / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

#! /usr/bin/python3

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_all_odds(n):
    number = str(n)
    for letter in number:
        if int(letter) % 2 == 0:
            return False
    return True

def podp_counter(n):
    counter = 0
    for i in range(2, n+1):
        if is_prime(i) and is_all_odds(i):
            counter += 1
    return counter


def odd_dig_primes(n):
    dig_primes = []
    below = n
    above = n + 1
    dig_primes.append(podp_counter(n))
    while True:
        if is_prime(below) and is_all_odds(below):
            dig_primes.append(below)
            break
        below -= 1
    while True:
        if is_prime(above) and is_all_odds(above):
            dig_primes.append(above)
            break
        above += 1
    return dig_primes
