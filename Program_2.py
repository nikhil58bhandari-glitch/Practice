        # Q1-> Power of 2 using anonymous function-:

# power = lambda n: 2 ** n
# n = int(input("Enter the power: "))
# print(power(n))

# num = int(input("Enter the Number : "))
# n = list(map(lambda x: 2 ** x, range(num + 1)))
# for i in range(num + 1):
#     print(f"2 power {i} is-: {n[i]}")


    # Q2-> Find Numbers divisible by another number

# num = int(input("Enter Number : "))
# upto = int(input("Enter a number upto we have to check : "))
# Division = list(filter(lambda x : x % num == 0, list(range(1, upto + 1))))
# print(f"The list of numbers which is divisible by {num} are {Division}")

     # Q3 -> Reverse Numbers -:

# num = int(input("enter the Number : "))
# print(int(str(num)[::-1]))
#
# num = int(input("enter the Number : "))
# rev_num = 0
#
# while num > 0:
#     rem = num % 10
#     rev_num = rem + (rev_num * 10)
#     num = num // 10
# print(rev_num)

     # Q4-> Count Number of digit in number

# num = int(input("Enter a number : "))
# print(len(str(num)))
#
# num = int(input("Enter a number : "))
# count = 0
# while num > 0:
#     num = num // 10
#     count = count + 1
# print(count)

     #  Q5-> Find HCF or GCD -:
    # (Highest Common Factor / Greatest Common factor)

# num1 =int(input("Enter thr Number : "))
# num2 = int(input("Enter the Number : "))

# while num2 != 0:
#     rem = num1 % num2
#     num1 = num2
#     num2 = rem
#
# print("HCF-: ", num1 )

# def Hcf(num1, num2):
#  while num2:
#     num1 , num2 = num2 , num1 % num2
#  return num1
# print(Hcf(num1,num2))

       # find LCM -:

a = int(input("Enter the Number : "))
b = int(input("Enter the number : "))

def hcf(a,b):
    while b:
     a , b = b, a % b
    return a
print(hcf(a,b))

def lcm(a,b):
    return (a * b) // hcf(a,b)

print(lcm(a,b))



