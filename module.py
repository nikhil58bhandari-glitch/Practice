  # Q1-> Print output without a new line->

print('i am naruto uzumaki', end = ' ')
print('i am gonna be a next hokage')

import sys
sys.stdout.write("hello ")
sys.stdout.write('praveen')

print()

  # Q2-> Get the class name of an instance -:

class myClass:
    pass

obj = myClass()   # Creating an object

class_name = type(obj).__name__
print(class_name)

class_Name = obj.__class__.__name__
print(class_Name)


   # Q3-> Random select an element from the list -:

import random
lis = [1,2,3,4,5,6,7,8,9]
print(random.choice(lis))

   # Q4-> Generate a random number random lib->

import random as r
print(r.randint(1,90))  # randint() generates a random integer between 1 and 90.
print(r.random())             # This gives a random decimal number from 0.0 up to, but not including, 1.0.
print(r.uniform(3,9))   # uniform() generates a random decimal number between 3 and 9.
print(r.choice("nikhil"))     # choice() selects one random item from a sequence.
print(r.choices('I goona be king of a pirates'))   # choices() selects one or more random items from a sequence.


    # Q5-> Display Calender->

import calendar
yy = int(input('Enter the year -:'))
mm = int(input('Enter the month -: '))
print()
print(calendar.month(yy, mm))
