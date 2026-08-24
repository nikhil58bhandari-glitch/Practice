        # Q1-> Power of 2 using anonymous function-:

# power = lambda n: 2 ** n
# n = int(input("Enter the power: "))
# print(power(n))

num = int(input("Enter the Number : "))
n = list(map(lambda x: 2 ** x, range(num + 1)))
for i in range(num + 1):
    print(f"2 power {i} is-: {n[i]}")