#!/usr/bin/python3
"""
    Program name: collatz.py
    Program purpose: Explore "the simplest impossible math problem" with Python.
    Date and version: 22-03-2026
    Author: Cameron Lamoureux
"""

# Print the result of calculations according to the Collatz sequence.
def collatz(number):
    if number % 2 == 0:
        outnum = number // 2
    elif number % 2 == 1:
        outnum = 3 * number + 1
    print(outnum)
    return outnum

# Perform the operations until the user input results in 1.
def main():
    print("The Collatz conjecture asserts that repeating the following two operations\
--divide by 2, if even; multiply by three then add one, if odd--\
will transform any positive integer into the number 1.\n")
    number = int(input("Enter a positive integer: "))
    while number != 1:
        number = collatz(number)


main()
