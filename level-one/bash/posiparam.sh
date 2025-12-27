#!/bin/bash
# Note: Script derived from GNU/Linux Desktop Support during first term of CST-Networking
# Description: this script provides examples of different shell variables and positional parameters.

myvar="tim"

echo "The value of \$myvar is : $myvar" 

echo "The name of the script is  : $0 "
echo "The number of command line arguments is : $# "
echo "All the command line arguments are :  $* "
echo "The first argument is $1 "
echo "The second is $2 "
echo "The third is $3 "
echo "The fourth is $4 "

