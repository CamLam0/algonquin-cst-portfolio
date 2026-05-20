#!/usr/bin/python3
'''
    Program name: guess_number.py
    Program purpose: Guess the number game
    Date and version: 02-06-2026, version 1.2
    Author: Cameron Lamoureux, lamo0318, section 012
'''

# Import random number generator module.
import random

# Define variables at program start.
secret = random.randint(1,9)
guess = -1
count = 1

# Prompt the user for repeated guesses unless they want to quit.
while guess != (0 or secret):
    guess = int(input("Guess a number between 1 and 9 (0 to quit): "))
    if guess == 0:
        print("Sorry you're giving up.")
        break
    elif guess > secret:
        print("Too high")
        count += 1
    elif guess < secret:
        print("Too low")
        count += 1
    else:
        print("You guessed it! It only took you", count, "tries.")

# Thank user before exit.
print("Thank you for playing.")
