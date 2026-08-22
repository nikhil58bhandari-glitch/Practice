operation = input("Enter the Calculator Symbol-: ")

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def exp(num1,num2):
    return num1 ** num2

def floordiv(num1,num2):
    return num1 // num2

while True:
 if operation in ["+", "-", "*", "/", "%", "**", "//"]:

    num1 = int(input("Enter the first number-: "))
    num2 = int(input("Enter the second number-: "))

    if operation == "+":
        print("addition -: ", add(num1,num2))

    elif operation == "-":
        print("subtaction -: ", sub(num1,num2))

    elif operation == "*":
        print("multiplication-: ",mul(num1,num2))

    elif operation == "/":
        if num2 == 0:
            print("cannot division by zero")
        else:
          print("division-: ", div(num1,num2))

    elif operation == "%":
        print("modulos-: ", mod(num1,num2))

    elif operation == "**":
        print("exponnentiotion-: ", exp(num1,num2))

    else:
        print("floordivision-: " , floordiv(num1,num2))

 else:
    print("enter invalid opration...")

 choice = input("Do you want tocontinue? y/n:  ")
 if choice.lower() == "n":
    break


