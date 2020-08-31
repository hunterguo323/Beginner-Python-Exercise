"""
Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same
forwards and backwards.)
"""

user_input = str(input('Please enter a string: '))
if user_input == user_input[::-1]:
    print("This string is a palindrome.")
else:
    print("This string is not a palindrome.")
