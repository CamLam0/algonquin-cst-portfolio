#!/usr/bin/python3
'''
    Program name: magic8Ball.py
    Program purpose: To tell the fortunes of the many.
    Program author: Al Sweigart in 'Automate the Boring Stuff with Python'
    Version & Date: 1.0, 03-06-2026
'''

import random

# Define the function that provides magical answers to questions.
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy; try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# Generate a random number, call the function, print the fortune.
'''
These three lines are equivalent to the one below.
    r = random.randint(1, 9)
    fortune = getAnswer(r)
    print(fortune)
'''
print(getAnswer(random.randint(1, 9)))
