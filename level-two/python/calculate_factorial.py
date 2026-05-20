#!/usr/bin/python3

"""
    Program name: calculate_factorial.py
    Program description: Python program to find the factorial of a number provided by the user.
    Date & Version: 02-02-2026, version 1.0
"""

# Prompt user for a number
number = int(input("Enter a number to calculate factorial: "))\

# Check for negative numbers or zero
if number < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1

# Calculate factorial of user's number, showing all results until desired number reached
for i in range(1,number + 1):
    factorial = factorial * i
    print("The factorial of", i,"is", factorial)
