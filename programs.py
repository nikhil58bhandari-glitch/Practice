 # Q1-> Print hello world

# print("hello, world!")

    # Q2-> ADD TWO NUMBERS-:

# def addNum(num1, num2):
#      return num1 + num2
#
# num1 = int(input("Enter the first number-: "))
# num2 = int(input("enter the second number-: "))
# result = addNum(num1,num2)
#
# print("The addition of num1 or num2 are-: {}".format(result))


  #  Q4-> FIND THE SQUARE AND CUBE -:

# def squear(n):
#  return n * n
# def cube(n):
#  return n ** 3
#
# n = int(input("Enter the number to find the Square nd Cube-: "))
#
# print("the square of the given value is -: " , squear(n))
# print("the cube of the given value is-:", cube(n))
#
    #  Q4 -> FIND THE SQUARE ROOT AND CUBE ROOT -:
#
# def squearRoot(n):
#  return n * (1/2)
# def cubeRoot(n):
#  return n ** (1/3)
#
# n = int(input("Enter the number to find the Square Root-: "))
#
# print("the square root of the given value is -: " , squearRoot(n))
# print("the cube root of the given value is-:", cubeRoot(n))


    # Q5 -> Check a number is +ve or -ve

# num = int(input("Enter the number-: "))
#
# if num < 0 :
#  print("The given number is negative")
#
# elif num > 0:
#  print("The given number is positive")
#
# else:
#  print("The given number is zero")

    # Q6 -> Largest among 3 numbers -:

# a = int(input("A -: "))
# b = int(input("B -: "))
# c = int(input("C -: "))
#
# if a > b and a > c:
#  print(f"{a} is largest among 3 numbers")
# elif b > a and b > c:
#  print(f"{b} is largest among 3 numbers")
# else:
#  print(f"{c} is largest among 3 numbers")

    #  Q7 -> Multiplication table-:

num = int(input("Enter which number table do you want-:"))

for i in range(1,11):
 print(num,"X",i,"=",num*i)

     # Q8 -> Swaping Numbers -:

# a = 100
# b = 200
# print("a-: ",a ,"b-: ", b)
#
# # a = a + b
# # b = a - b
# # a = a - b
# # a = b
# # b = a
#
# print("a-: ",a ,"b-: ", b)

      #  Q9 -> Area of triangle

# slection = int(input("Apply 1 if is the right angle triangle else 0 : "))
#
# def right_angle(b,h):
#     area = 0.5 * b * h   # (1/2) * b * h
#     return area
#
# def equilateral_angle(side):
#     area = ((3 ** 0.5)/4) * side * side
#     return area
#
# if slection == 1:
#     heigth = int(input("Enter the height of the triangle-: "))
#     base = int(input("Enter the base of the tringle-: "))40
#     print("The area of the right-angle tringale is -: " , right_angle(base,heigth))
#
# else:
#     side = int(input("Enter the side of the triangle-: "))
#     print("The area of the equilateral-angle triangle is -:", equilateral_angle(side))
#
#
