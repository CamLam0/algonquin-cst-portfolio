#!/usr/bin/python3
'''
    Program name: abcdCallStack.py
    Program purpose: Provide an overview of the function call stack.
    Program author: Al Sweigart in 'Automate the Boring Stuff with Python'
    Version & Date: 1.0, 03-06-2026
'''

# Four functions, each calling others within each other.
# Run the program to see the stack in order
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()
