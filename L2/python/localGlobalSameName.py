#!/usr/bin/python3
'''
    Program name: localGlobalSameName.py
    Program purpose: Show what happens when local and global variable names are the same.
    Program author: Al Sweigart in 'Automate the Boring Stuff with Python'
    Version & Date: 1.0, 03-06-2026
'''

# Prints output of three separate variables, each named eggs.
# Ouput depends on the scope of each variable. It can be either local or global.
# When a function returns, it's local scope is erased.
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)     # prints 'global'

