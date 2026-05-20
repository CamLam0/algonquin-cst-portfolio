#!/usr/bin/python3
"""
    Program name: exponentiate.py
    Program purpose: Square and cube numbers provided by the user.
    Date and version: 20-02-2026
    Author: Cameron Lamoureux, lamo0318, section 012
"""

# Get a number from the user.
def get_integer(prompt = "Enter a number: "):
    user_num = int(input(prompt))
    return user_num

# Square a number.
def square(num):
    square_num = num * num
    return square_num

# Cube a number.
def cube(num):
    cube_num = num ** 3
    return cube_num

# Display the squared and cubed output of a user-given number.
def main():
    # Display purpose, prompting for confirmation.
    print("This program squares and cubes an integer.")
    confirm = input("Would you like to proceed? [y/n]: ").lower()

    # Display the results of square and cube operations; prompt for repeat.
    while confirm != "n":
        user_num = get_integer()
        if user_num == 0:
            print('0')
        elif user_num == 1:
            print('1')
        else:
            square_num = square(user_num)
            cube_num = cube(user_num)
            print(f"{user_num} squared equals {square_num}, cubed equals {cube_num}")

        confirm = input("Would you like to go again? [y/n]: ").lower()

main()

# Thank the user before exit.
print("Thank you for squaring and cubing today.")
