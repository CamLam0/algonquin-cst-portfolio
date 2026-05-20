#!/usr/bin/python3
'''
    Program name: globalStatement.py
    Program purpose: Call a global variable from within a function
    Program author: Al Sweigart in 'Automate the Boring Stuff with Python'
    Version & Date: 1.0, 03-06-2026
'''

# Rewrite the global variable (eggs) to 'spam'
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
