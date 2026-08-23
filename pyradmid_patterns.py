  #  square pattern

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n):
#         print("*", end= " ")
#     print()
#
#            #
# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i+1):
#           print("*", end=" ")
#     print()
#
#           #
# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n-i):
#           print("*", end=" ")
#     print()

       #
n = 5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n - i ):
        print("*", end=" ")
    print()
print()

       #
n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    print()
print()

         #
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ",end="")
    # for k in range(2 * i + 1):
    #     print("*", end="")
    print()
print()

        #
n = 5
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("* ",end="")
    print()
print()

         #
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("* ",end="")
    print()
print()

          #
n = 5
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("* ", end="")
    print()
for i in range(n):
    for j in range(n - i -1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ",end="")
    print()
print()

          #
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print()



n = 5
for i in range(n):
    for j in range(n - i - 1):
         print(" ", end = "")
    for k in range(i + 1):
        if k == 0 or k == i or i == n -1:
            print("* ",end="")
        else:
            print("  ", end = "")
    print()





