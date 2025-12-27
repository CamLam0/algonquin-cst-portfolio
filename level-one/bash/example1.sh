#!/bin/bash
# Name: readstr.sh
# Note: Derived from GNU/Linux Desktop Support lecture slides during my first term in CST-Networking
# Comparing two strings entered by user

read -p "Enter 1st string: " -n 10 string1
echo ""
read -p "Enter 2nd string: " string2

echo $string1 $string2
