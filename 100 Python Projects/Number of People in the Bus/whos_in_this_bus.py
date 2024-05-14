#! /usr/bin/python
# **************************************************************************** #
#                                                                 __           #
#    whos_in_this_bus.py                                         / _)          #
#                                                       _/\/\/\_/ /            #
#          By: pedro_mota                             _|         /             #
#      Github: github.com/peterbikes                _|  (  | (  |              #
#    Linkedin: linkedin.com/in/pedrosmpm/         /__.-'|_|--|_|               #
#                                                                              #
# **************************************************************************** #

"""

CodeWars exercise: codewars.com/users/peterbikes

There is a bus moving in the city which takes and drops some people at each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

"""

def number(bus_stops):
    ppl = 0
    for stop in bus_stops:
        ppl += stop[0] - stop[1]

    return ppl

# variable storing list of passangers:
#[<people that get in>,<people that get out>]
bus_stops = [3,2],[5,4],[10,3]

print("This is a code wars exercise, view file comments to see more information!")
print("Example list:", bus_stops)
if(number(bus_stops) >= 0):
    print("There are", number(bus_stops), "people in this bus.")
else:
    print("There is a negative number of people in the bus :0")
print("Edit this file to insert your own list.")
