#!/usr/bin/python3

"""
    Program name: calculate_dec.py
    Program purpose: Perform calculations based on user input.
    Date and version: 29-01-2026
    Author: Cameron Lamoureux, lamo0318, section 012
"""

# Prompt the user for input.
print("+, -, *, /")
operator = str(input("Please select an operator: "))
operand1 = float(input("Enter a decimal number: "))
operand2 = float(input("Enter another decimal number: "))

# Calculate user-specified operations.
# Performs addition if selected
if operator.strip() == "+":
    print(f"The first operand {operand1} plus the second operand {operand2} = {operand1 + operand2}")

# Performs subtraction if selected
elif operator.strip() == "-":
    print(f"The first operand {operand1} minus the second operand {operand2} = {operand1 - operand2}")

# Performs multiplication if selected
elif operator.strip() == "*":
    print(f"The first operand {operand1} times the second operand {operand2} = {operand1 * operand2}")

# Performs division if selected
elif operator.strip() == "/":
    print(f"The first operand {operand1} divided by the second operand {operand2} = {operand1 / operand2}")

# Informs user of invalid operator selection
else:
    print("Invalid selection.")

# Thank the user before exit
print("Thank you.")
