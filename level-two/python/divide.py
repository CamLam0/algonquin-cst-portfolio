#!/usr/bin/python3

'''
    Program name: divide.py
    Purpose: Perform division.
    Author: Cameron Lamoureux
    Date: 20-02-2026
    Version: 2.0
'''

# Greet user.
first_name = input("Enter first name: ")
print(f"Welcome {first_name}")

# Repeated division after user confirmation.
confirm = input("Would you like to proceed? [y/n]: ").lower()

while confirm != "n":
    # Prompt for operands.
    dividend = float(input("Enter dividend: "))
    divisor  = 0

    # Divide operands, ensuring user cannot divide by zero.
    while divisor == 0:
            divisor  = float(input("Enter non-zero divisor: "))
    quotient = dividend / divisor

    # Display the results of the divison, then prompt for repeat.
    print( f"Quotient is: {quotient}" )
    confirm = input("Would you like to proceed? [y/n]: ").lower()

# Display closing message.
print("Thank you.")
