        # Q1-> Power of 2 using anonymous function-:

# power = lambda n: 2 ** n
# n = int(input("Enter the power: "))
# print(power(n))

# num = int(input("Enter the Number : "))
# n = list(map(lambda x: 2 ** x, range(num + 1)))
# for i in range(num + 1):
#     print(f"2 power {i} is-: {n[i]}")


    # Q2-> Find Numbers divisible by another number

num = int(input("Enter Number : "))
upto = int(input("Enter a number upto we have to check : "))
Division = list(filter(lambda x : x % num == 0, list(range(1, upto + 1))))
print(f"The list of numbers which is divisible by {num} are {Division}")