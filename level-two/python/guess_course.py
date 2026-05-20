#!/usr/bin/python3

"""
    Program name: guess_course.py
    Program purpose: Check if user knows the course code for Programming Fundamentals
    Date and version: 29-January-2026
    Author: Cameron Lamoureux, lamo0318, section 012
"""

# constant variables
COURSE_CODE = "CST8324"

# Prompt the user for their guess
course_guess = str(input("What is the course number? (q to quit) : "))

# Iterate guesses until user gets it or quits
while course_guess != COURSE_CODE and course_guess.lower() != "q":
    course_guess = str(input("What is the course number? (q to quit) : "))

    if course_guess == COURSE_CODE:
        print("Correct! Great guess.")
    elif course_guess.lower() == "q":
        print("Exiting...")
    else:
        course_guess = str(input("Incorrect. Take another guess? (q to quit) : "))

# Thank the user before exit
print("Thank you.")
