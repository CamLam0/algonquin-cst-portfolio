#!/usr/bin/python3
"""
    Program name: calculate_average.py
    Program purpose: Calculate the sum and the average of numbers input by user.
    Date and version: 23-03-2026
    Author: Cameron Lamoureux, lamo0318, section 012
"""

# Display calculation options.
def show_menu():
    print("add")
    print("average")
    print("(q)uit")

# Prompt the user for a list of numbers.
def get_floatlist(prompt):
    numlist = float(prompt.split())
    for num in numlist:
        numlist[numlist.index(num)] = float(num)
    return numlist

# Perform addition on user-provided list of numbers.
def add_numlist(numlist):
    total = sum(numlist)
    return total

# Calculates the average of user-provided list of numbers.
def cal_avg(numlist):
    total = add_numlist(numlist)
    items = len(numlist)
    avg = total / items
    return avg

# Perform calculations based on user selection.s
def main():
    choice = ""
    while choice != "q":
        show_menu()
        choice = input("Please select an option from the menu above: ")
        if choice == "add":
            numlist = get_floatlist(input("Enter numbers, space separated: "))
            total = add_numlist(numlist)
            print(f"The total is {total}")
        elif choice == "average":
            numlist = get_floatlist(input("Enter numbers, space separated: "))
            avg = cal_avg(numlist)
            print(f"The average is {avg}")
        elif choice != "q":
            print("Invalid selection. Please try again.")

main()
