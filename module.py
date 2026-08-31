  # Q1-> Print output without a new line->

# print('i am naruto uzumaki', end = ' ')
# print('i am gonna be a next hokage')
#
# import sys
# sys.stdout.write("hello ")
# sys.stdout.write('praveen')
#
# print()
#
#   # Q2-> Get the class name of an instance -:
#
# class myClass:
#     pass
#
# obj = myClass()   # Creating an object
#
# class_name = type(obj).__name__
# print(class_name)
#
# class_Name = obj.__class__.__name__
# print(class_Name)
#
#
#    # Q3-> Random select an element from the list -:
#
# import random
# lis = [1,2,3,4,5,6,7,8,9]
# print(random.choice(lis))
#
#    # Q4-> Generate a random number random lib->
       # random->

# import random as r
# print(r.randint(1,90))  # randint() generates a random integer between 1 and 90.
# print(r.random())             # This gives a random decimal number from 0.0 up to, but not including, 1.0.
# print(r.uniform(3,9))   # uniform() generates a random decimal number between 3 and 9.
# print(r.choice("nikhil"))     # choice() selects one random item from a sequence.
# print(r.choices('I goona be king of a pirates'))   # choices() selects one or more random items from a sequence.
#
#
#     # Q5-> Display Calender->
#
# import calendar
# yy = int(input('Enter the year -:'))
# mm = int(input('Enter the month -: '))
# print()
# print(calendar.month(yy, mm))


#   # math->
#
# import math
#
# print(math.sqrt(25))
# print(math.pow(2,4))
# print(math.factorial(5))

    # string->
# import string
# print(string.punctuation)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

     # datetime->
# import datetime
# print(datetime.datetime.today())

    # os ->
# import os
# print(os.getcwd())     # Get Current Working Directory.
# print(os.listdir())    # to see files/folders in the current directory.

    # sys->
# import sys
# sys.stdout.write('hello ')   # sys gives you information and controls related to the Python interpreter/system.

     # json->
# import json
# data = '{"name" : "nikhil", "age" : 22}'
# result = json.loads(data)
# print(result['name'])
# print(result)


   # Represent Enum->

from enum import Enum
class color(Enum):  # define color enum
    red = 1
    green = 2
    blue = 3

print(color.red)   # Accessing Enum member

print(color.green.value)  # print enum value

for x in color:   # Go through every member inside the Color Enum.
    print(x)

print(color.red == color.red)
print(color.red == color.green)



   # Shuffle deck of cards

import itertools, random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# cards = [(suits, ranks) for suit in suits for rank in ranks]   # It creates every possible combination of:
cards = []
# for suit in suits:
#     for rank in ranks:
#         cards.append((suit, rank))
cards = list(itertools.product(suits,ranks)) #  Give me every possible combination of one item from suits and one item from ranks.
random.shuffle(cards)
for i in range(5):
    print(cards[i][0], 'of', cards[i][1])


       # Compute all the permutations of the sting ->
from itertools import permutations
text = 'abc'
letters = permutations(text)   # "Give me every possible ordering of the characters in abc."
words = [''.join(letter) for letter in letters]
for word in words:
    print(word,end=' ')



    # Creating a countdowns timer -:

import time

def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes_remaining = seconds // 60
        seconds_remaining = seconds % 60
        print(f'{minutes_remaining:02d} : {seconds_remaining:02d}')
        time.sleep(1)   # Pause the program for 1 second.
        seconds -= 1
    print('time is up!')
timer(1)

  # Measure the Elapsed time->
start = time.time()
time.sleep(3)
end = time.time()
elapsed = end - start
print(f"{elapsed:2f}")