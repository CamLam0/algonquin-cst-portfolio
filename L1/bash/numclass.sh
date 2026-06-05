#!/bin/bash
# Note: Script derived from GNU/Linux Desktop Support during first term of CST-Networking
# Description: This script asks the user to enter any positive number,
# script will classify it as small, medium or large.

read -p "Enter a number: " n

if [ "$n" -eq 0 ]; then
	size='empty'
elif [ "$n" -lt 0 ]; then
	size='negative'
elif [ "$n" -le 100 ]; then
	size='small'
elif [ "$n" -le 10000 ]; then
	size='medium'
else
	size='large'
fi

echo "$n has been classified as $size"


