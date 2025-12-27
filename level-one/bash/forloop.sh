#!/bin/bash
# Note: Derived from GNU/Linux Desktop Support lecture slides during my first term in CST-Networking
# Description: this script uses two for loops to show the difference between implicit and explicit arguments in bash.
# implicit list of words come from command line arguments; includes error checking
name="$1 $2 $3"

if [ $# -ne 3 ]; then 
	echo "Must enter first, middle and last name."
fi

echo "Your name is $name"


# explicit list of words come from predefined lists, arrays, etc.
AR=('james' 'thomas' 'lauren' 'onyx' 'steven' 'joe' 'amy')
echo "${#AR[@]} people are currently in line."
for i in "${!AR[@]}"; do
	echo "${AR[$i]} is $((i + 1)) in line"
done
