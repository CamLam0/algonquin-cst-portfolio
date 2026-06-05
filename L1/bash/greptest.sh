#!/bin/bash
# Note: Script derived from GNU/Linux Desktop Support slides during first CST-Networking semester
# Description: use regular expressions to test positional parameters, identifying what kind of input was provided
re='^[0-9]'
if ! [[ $1 =~ $re ]]; then
	echo "error: Not a number" 
elif [[ $1 =~ ^[0-9{1,3}[:alpha:] ]]; then
	echo " is a number"
elif [[ $1 = [[:alnum:]] ]]; then
	echo "Entered value is alphanumberic"
elif [[ $1 =~ ^.+@.+\.\w$ ]]; then
	echo "Entered value is an email"
elif [ "$1" = "[[:digit:]]" ]; then
	echo "Entered value is a digit"
elif [[ $1 = [[:punct:]] ]]; then
	echo "Entered value is a special character"
else
	echo "Please enter a single positional parameter"
fi
