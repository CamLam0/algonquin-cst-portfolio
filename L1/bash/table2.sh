#!/bin/bash
# Note: Script derived from GNU/Linux Desktop Support during first term of CST-Networking
# Description: this script makes a multiplication table based on two given positional parameters (# and range #)


echo "Enter a number: "

read a

echo "Enter the range for this number to be multiplied: "

read b

echo "*******************************"

echo "  This is a $a time table"

echo "*******************************"
i=1
while [ $i -le $a ]; do
	echo "the sum of $a times $i is $(($a * $i))"
	i=$(($i + 1))
done

