#!/bin/bash
# Name: errors.sh
# Note: Derived from GNU/Linux Desktop Support lecture slides during my first term in CST-Networking
# Description: this script will illustrate some best practices regarding error messages in bash
# specifically, ensure that
# 1) script name is shown
# 2) the specific cause of the error is shown
# 3) the number of errors is shown

if [ $# -lt 1 ]; then
	echo "Enter a positional parameter"
elif [ $# -gt 1 ]; then
	echo 1>&2 "$0: Error: expecting one posiparam, found $# ($*)"
else 
	echo "Your posiparam is $1"
fi

