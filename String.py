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

s = 'Ande Sai Preveen'
s1 = s[4:8]
s2 = s[5:]
s3 = s[:8:-1]
print('S1:', s1)
print('S2:', s2)
print('S3:', s3)


   # Q7-> sort words with alphabetical order-:

alphabets = ['hai','i','had','many', 'hopes', 'on', 'tec', 'compony', 'for', 'that',
            'i', 'had', 'prepared', 'very', 'much']

sorted_one = sorted(alphabets)
print(sorted_one)

alphabets = ['hai','i','had','many', 'hopes', 'on', 'tec', 'compony', 'for', 'that',
            'i', 'had', 'prepared', 'very', 'much']
for i in range(len(alphabets)):
    for j in range(len(alphabets)-i-1):
        if alphabets[j] > alphabets[j + 1]:
            alphabets[j], alphabets[j + 1] =  alphabets[j + 1], alphabets[j]
print(alphabets)

