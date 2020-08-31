'''
Create a program that asks the user to enter their name and
their age. Print out a message addressed to them that tells
them the year that they will turn 100 years old.
'''
import datetime

while True:
    name = input('Please enter your name: ')
    age = input('Please enter your age: ')
    repeat = input('How many times would you like to see the result: ')

    now = datetime.datetime.now()
    this_year = now.year
    message = f'In year {this_year-int(age)+100}, {name.title()} will be 100 years old.'
    for n in range(int(repeat)):
        print(message)
    in_program = input("Enter 'q' to quit the program.\n")

    if in_program == 'q':
        break
