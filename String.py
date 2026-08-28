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

character  = input("Enter the character -: ")
ascii_value = ord(character)     # ord() gives the Unicode number of a character
chr_value = chr(ascii_value)     # chr() does the opposite of ord().
print(f'Unicode value of {chr_value} is {ascii_value}')


    # Q4-> String is Palindrome or not -:

string = input("Enter the String -: ")
if string == string[::-1]:
    print("String is Palindrome")
else:
    print("Not Palindrome")