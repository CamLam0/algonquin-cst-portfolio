#!/bin/bash
# Note: Script derived from GNU/Linux Desktop Support slides during first semester of CST-Networking 
# Description: Example for input validation using regular expressions (regex)
# variables are quoted to avoid misinterpretation by the shell

if [[ "$1" =~ ^[0-9]+$ ]] ; then 
	echo "this is a number"
elif [[ "$1" =~ ^[[:alpha:]]{1,}$ ]]; then
	echo "this is a string"
elif [[ "$1" =~ ^[[:alpha:]][[:digit:]][[:alpha:]]\ ?[[:digit:]][[:alpha:]][[:digit:]]$ ]] ; then
	echo "this is a valid postal code"
elif [[ "$1" =~ ^[[:alpha:][:punct:]]+$ ]]; then
	echo "this string contains special characters"
elif [[ "$1" =~ ^[[:alpha:][:digit:]]+\@algonquincollege\.live$ ]]; then
	echo "this is a valid algonquin college email address"
fi

