#!/usr/bin/python3
'''
    Program name: select_venue.py
    Program purpose: Provide the user with venue options for Saturday nights
    Program editor: Cameron Lamoureux, lamo0318, section 012
    Date & version: 02-09-2026, version 2.0
'''

# Prompt user to select venue or quit.
decision = input("Want to choose a venue for Saturday night? [y/n]: ").lower()

# Provide the user with venue options to choose from.
if decision == 'y':
    venue = input("Enter venue (restaurant, movie, bowling): ").lower()
    if venue == "restaurant":
        ethnic = input("Italian or Chinese? ").lower()
        if ethnic == "italian":
            print("Pasta it is!")
        elif ethnic == "chinese":
            print("How about Dim Sum?!")
        else:
            print("You chose neither of these fantastic options.")
    elif venue == "movie":
        print("Let’s pick a genre.")
        movie_choice = str(input("(A)ction, (C)omedy, (D)rama: ")).lower()
        if movie_choice == "a":
            print("You chose Action!")
        elif movie_choice == "c":
            print("You chose Comedy!")
        elif movie_choice == "d":
            print("You chose Drama!")
        else:
            print("That's not a valid genre.")
    elif venue == "bowling":
        print("Let's play ten-pin at the ARC!")
    else:
        print("Sorry you're so picky.")
else:
    print("Maybe next week...")

# Thank the user before exit
print("Thank you. Have a nice day.")
