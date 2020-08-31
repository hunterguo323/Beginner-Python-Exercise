"""
Ask the user for a number. Depending on whether the number is
 even or odd, print out an appropriate message to the user.

Extras:

If the number is a multiple of 4, print out a different message.

Ask the user for two numbers: one number to check (call it num)
and one number to divide by (check). If check divides evenly
into num, tell that to the user. If not, print a different
appropriate message.
"""

while True:
    num = int(input('Please enter a number: '))
    check = int(input('Please enter a divider: '))

    if num % 4 == 0:
        print(f'Number {num} is a multiple of 4')
    elif num % check == 0:
        print(f'Number {num} can divide {check} evenly.')
    else: print(f'Number {num} can not divide {check} evenly.')

    in_program = input('Would you like to input more numbers?\nEnter "q" to quit.')
    if in_program == 'q':
        break
