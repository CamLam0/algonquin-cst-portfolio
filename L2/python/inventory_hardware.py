#!/usr/bin/python3
"""
    Program name: inventory_hardware.py
    Program purpose: Manage a simple hardware inventory.
    Date and version: 23-03-2026
    Author: Cameron Lamoureux, lamo0318, section 012
"""
hardware_inventory = {
    "Laptop": 18,
    "Printer": 3,
    "Monitor": 8,
    "Desktop": 8,
    "Keyboard": 6,
    "Mouse": 21
}

def show_inventory():
    print("Hardware inventory")
    for key, value in hardware_inventory.items():
        print(key, "-", value)

def main():
    show_inventory()
    item = input("Enter hardware item to add/update: ")
    if hardware_inventory.get(item) != None:
        print("Updating inventory for", item)
        quantity = int(input("Enter quantity: "))
        hardware_inventory.update({item: quantity})
        print(item, "quantity updated to:", hardware_inventory.get(item))

main()
