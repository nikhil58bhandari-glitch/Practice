  #  Q1-> Parse a string to a float or int -:

# string_in = '3.14'
# string_in = '3.14pi'
#
# try:
#     float_in = float(string_in)
#     print(float_in)
#
# except ValueError as e :
#    print('Exception raised on ', e)


   # Q2-> Create a long multiline String -:

# long_string = '''This is a long multiline string.
# It spans across multiple lines.
# You can include line breaks and formatting within the string.
#
# Here's an example of a bulleted list:
# - Milk
# - Eggs
# - Bread
# - Apples
# Just make sure to enclose the string in triple quotes.'''
#
# print(long_string)


     # Q3-> Ascii value of a character -:

# character  = input("Enter the character -: ")
# ascii_value = ord(character)     # ord() gives the Unicode number of a character
# chr_value = chr(ascii_value)     # chr() does the opposite of ord().
# print(f'Unicode value of {chr_value} is {ascii_value}')


    # Q4-> String is Palindrome or not -:

# string = input("Enter the String -: ")
# if string == string[::-1]:
#     print("String is Palindrome")
# else:
#     print("Not Palindrome")


   # Q5-: count the number of each vowel-:

# words = input("Enter the String -: ").upper()
# A = E = I = O = U = 0
# for i in words:
#     if i == 'A':
#       A += 1
#     elif i == 'E':
#         E += 1
#     elif i == 'I':
#         I += 1
#     elif i == 'O':
#         O += 1
#     elif i == 'U':
#         U += 1
#     else:
#         pass
# print(f"A = {A} E = {E} I = {I} O = {O} U = {U}")


  # Q6-> Get SubString of a string-:

# s = 'Ande Sai Preveen'
# s1 = s[4:8]
# s2 = s[5:]
# s3 = s[:8:-1]
# print('S1:', s1)
# print('S2:', s2)
# print('S3:', s3)


   # Q7-> sort words with alphabetical order-:

# alphabets = ['hai','i','had','many', 'hopes', 'on', 'tec', 'compony', 'for', 'that',
#             'i', 'had', 'prepared', 'very', 'much']
#
# sorted_one = sorted(alphabets)
# print(sorted_one)
#
# alphabets = ['hai','i','had','many', 'hopes', 'on', 'tec', 'compony', 'for', 'that',
#             'i', 'had', 'prepared', 'very', 'much']
# for i in range(len(alphabets)):
#     for j in range(len(alphabets)-i-1):
#         if alphabets[j] > alphabets[j + 1]:
#             alphabets[j], alphabets[j + 1] =  alphabets[j + 1], alphabets[j]
# print(alphabets)


  # Q7->  Trim Whitespace from a sting -:

# string = "Hai sai praveen"
# trim = ''
# for i in string:
#     if i != ' ':
#         trim = trim + i
# print(trim)
#
# string = "            hai sai praveen"
# print(string.strip())
# print(string.rstrip())
# print(string.lstrip())



   # Q8-> Convert bytes to string-:

# byte_code = b'Hai praveen'
# decode_code = byte_code.decode()
# print(type(byte_code))
# print(type(decode_code))


   # Q9-: check if two string are anagram-:

# string1 = "listen"
# string2 = "silent"
# string1 = string1.replace(' ','').lower()
# string2 = string2.replace(' ','').lower()
# if sorted(string1) == sorted(string2):
#     print("strings are Anagram")
# else:
#     print("not anagram")


    # Q10-> Capitalise the first character of string-:

# text = "hai my name is nikhil. now i am going to create a capitalised text"
# words = text.split()
# text = [word[0].upper() + word[1:] for word in words]
# text = " ".join(text)   # Join all the elements using a space " " between them
# print(text)
#
# name = 'one-Piece'
# print(name[0].upper() + name[1:])

# text = "hai my name is nikhil. now i am going to create a capitalised text"
# print(text.capitalize())    # It makes only the first character of the entire string uppercase.
# print(text.title())    # It makes the first letter of every word uppercase.


    # Q11-> Check if string is a Number(float)

def is_num(input):
    return isinstance(input,str)   # "Is this value of this particular type?"

def is_num2(input):
    return input.isdigit()      # isdigit() checks whether a string contains only digits.

def is_num3(input):
    return input.isnumeric()   # isnumeric() is similar to isdigit().

def is_num4(input):      # It tries to convert the value into a floating-point number.
    try:
        float(input)
        return True
    except:
        return False

print(is_num('123'))
print(is_num('hello'))
print(is_num(123))
print(is_num2('123'))
print(is_num3('123'))
print(is_num4('234'))