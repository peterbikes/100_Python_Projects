#! /usr/bin/python

# Exercise from codewars.com: Simple Pig Latin


def pig_it(text):
    ay = 'ay'
    pigged = ''
    list = text.split()
    i = 0
    while(i < len(list)):
        if list[i].isalpha():
         pigged += list[i][1:len(list[i])] + list[i][0] + ay
        else:
         pigged += list[i]
        if i < len(list) -1:
         pigged += ' ' 
        i+=1
    return(pigged)

string = input("Give me a delicious string: ")
print(pig_it(string))
