#!/usr/bin/python3
# Testing program for exception handling

'''
    Program name: divide.py
    Purpose: Perform division.
    Author: Cameron Lamoureux
    Date: 30-03-2026
    Version: 1.0
'''

def get_float(prompt):
    return float(input(prompt))

def divide(dividend, divisor):
    return dividend / divisor

# Prompt for operands.
dividend = get_float("Enter dividend: ")
divisor  = get_float("Enter non-zero divisor: ")

# Divide operands.
quotient = divide(dividend, divisor)

# Display the results of the division.
print( f"Quotient is: {quotient}" )

# Display closing message.
print("Thank you.")
