import numbers

       #  Q1-> Solve Quadratic Equation **
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
#
# if a == 0:
#     print("invalid quadratic eqation")
# else:
#     discriminamt = (b ** 2) - 4 * a * c
#     squrt = discriminamt ** (1/2)
#     denominator = 2 * a
#     if discriminamt > 0:
#         x1 = -b + squrt / denominator
#         x2 = -b + squrt / denominator
#         print("Two real roots")
#         print("Roots", x1, "and", x2)
#     elif discriminamt  == 0:
#         print(" one Real and same Root ")
#         print("Roots are-: " , -b / denominator)
#     else:
#         print("complex root")

     #  Q2-> convert kilomtr into miles
# miles = float(input("Enter the mile to convert into kilometers-: "))
# kilometers = miles * 1.60934
# print(f"{miles} miles are equeal to {kilometers} kilometers")
#
# kilometers = float(input("Enter the kilometers to convert into miles-: "))
# miles = kilometers * 0.6215
# print(f"{kilometers} kilometers are equales to {miles} miles")

      # Q3-> check the number is even or odd
# number = int(input("Enter the number-: "))
# def even_num(num):
#     num=  num % 2 == 0
#     return num
# def is_odd(num):
#     return num % 2 == 1
# if even_num(number):
#     print("Even Number")
# else:
#     print("Odd Number")
#

     # Q4 -> check leap year or not
# def leap(year):
#     return year % 4 == 0
# year = int(input("Enter the year: "))
# if leap(year):
#     print("this is a leap year...")
# else:
#     print("this is not a leap year...")

    # Q5 -> sum of all natural number-:
# number = int(input("Enter the number upto-: "))
# sum = 0
# for i in range(number+1):
#     sum = sum + i
# print("sum is:",sum)


     #  Q6 -> factorial of a number
# number = int(input("Enter the number which you want to find out factorial-: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial = factorial * i
# print(factorial)

   #  Q7-> prime number -:
num = int(input("Enter the numbre-: "))

if num < 2:
    print("the numbers is not a prime number")
else:
    for i in range(2,num  ):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
            print(f"{num} is a prime number")
