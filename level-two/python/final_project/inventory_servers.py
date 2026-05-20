#!/usr/bin/python3
"""
    Program name: inventory_servers.py
    Program purpose: Manage server data across CSV and JSON formats.
    Date and version: 09-04-2026, version 2.0
    Author: Cameron Lamoureux, lamo0318, section 012
"""
import sys
import csv
import json

HOSTS_CSV = "hosts.csv"
HOSTS_JSON = "hosts.json"

########################
# Function definitions #
########################

# Purpose:   Get attribute list.
# Parameter: server data
# Return:    list of attributes
#
def get_keys(server_list):
    return list(server_list[0].keys())

# Purpose:   Find servers based on search criteria.
# Parameter: server data, search criteria
# Return:    matching servers
#
def search_server(server_list, search_string):
    matching_servers = []
    for server in server_list:
        for value in server.values():
            if search_string in value:
                matching_servers.append(server)
                break
    return matching_servers

# Purpose:   Add server to list based on user input.
# Parameter: server data, server information
# Return:    updated server data
#
def add_server(server_list, server_info):
    server_list.append(server_info)
    return server_list

# Purpose:    Write a JSON file.
# Parameters: destination file, server data
# Return:     none
#
def write_json(output_file, server_data):
    try:
        with open(output_file, 'w') as json_file:
            json.dump(server_data, json_file, indent=4)
    except Exception as e:
        print("Error writing JSON file:", e)

# Purpose:    Read a CSV file.
# Parameters: file path
# Return:     file data as list of dictionaries
#
def read_csv(input_file):
    data = []
    try:
        with open(input_file, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)
            for row in csv_data:
                data.append(row)
        return data
    except FileNotFoundError:
        print("File not found. \nExiting program.")
        sys.exit(1)
    except PermissionError:
        print("Permission error. \nExiting program")
        sys.exit(1)
    except OSError as ose:
        print("Cannot open file:", ose, "\nExiting program.")
        sys.exit(1)
    except Exception as e:
        print("Error:", e, "\nExiting program.")
        sys.exit(1)
    return None

# Purpose:   Display menu options.
# Parameter: none
# Return:    none
#
def show_menu():
    print("\n~ Server Management Menu: ~ \n"
          "\tL - List all servers\n"
          "\tS - Search servers\n"
          "\tA - Add server\n"
          "\tD - Delete server\n"
          "\tQ - Quit\n")
    return

# Purpose:   Get menu option.
# Parameter: prompt
# Return:    selected menu option
#
def get_menu_option(prompt):
    return input(prompt).upper()

# Purpose:   Get search string.
# Parameter: prompt
# Return:    search criteria
#
def get_search_string(prompt):
    return input(prompt).lower()

# Purpose:   List all servers based on search criteria.
# Parameter: server data, search criteria
# Return:    none
#
def list_servers(server_list, key = None):
    for row in server_list:
        if key:
            print( key, ":", row.get(key) )
        else:
            print(row)
    return

# Purpose:   Get server information.
# Parameter: prompt, attributes
# Return:    server information
#
def get_server_info(prompt, keys):
    server_info = {}
    print(prompt)
    for key in keys:
        server_value = input(key + ": ").lower()
        server_info.update({key:server_value})
    return server_info

# Purpose:   Delete server.
# Parameter: server data, server information
# Return:    updated server data
#
def delete_server(server_list, row):
    server_list.remove(row)
    return server_list

# Purpose:   Find server based on FQDN.
# Parameter: server data, fqdn
# Return:    matching server or False
# 
def find_fqdn(server_list, fqdn):
    for row in server_list:
        if fqdn in row["hostname"] + "." + row["domain"]:
            return row
    return False

################
# Main program #
################

# Import server information from csv file.
server_data = read_csv(HOSTS_CSV)

# Prompt user for menu selection.
show_menu()
menu_option = get_menu_option("Enter menu option: ").upper()

# Perform user-selected action, unless user quits.
while menu_option != "Q":

    # List server information based on search criteria.
    if menu_option == "L":
        print("\nListing servers.")
        key_list = get_keys(server_data)
        print( "Search criteria options:", key_list )
        search_key = get_search_string("Enter listing criteria: ")
        list_servers(server_data, search_key)

    # Search server information for specific strings.
    elif menu_option == "S":
        print("\nReady to search for server.")
        search_string = get_search_string("Enter search criteria: ")
        matching_servers = search_server(server_data, search_string)
        if matching_servers:
            list_servers(matching_servers)
        else:
            print("No servers found.")
 
    # Add a server to the dictionary with user-input values.
    elif menu_option == "A":
        print("\nReady to add server.")
        key_list = get_keys(server_data)
        server_info = get_server_info("Enter server information:", key_list)
        server_data = add_server(server_data, server_info)
        print("Added", server_data[-1])

    # Delete a server from the dictionary.
    elif menu_option == "D":
        print("\nReady to delete server based on FQDN.")
        fqdn = get_search_string("Enter FQDN for server to delete: ")
        row = find_fqdn(server_data, fqdn)
        if row:
            server_data = delete_server(server_data, row)
        else:
            print("Server record does not exist.")

    # Display error message.
    else:
        print("Invalid menu option.")

    # Display menu and prompt user for selection.
    show_menu()
    menu_option = get_menu_option("Enter menu option: ").upper()

# Output server information to JSON file.
write_json(HOSTS_JSON, server_data)

# Display exit message.
print("\nExiting server management program.")
