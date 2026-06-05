#!/bin/bash
# Note: Script derived from GNU/Linux Desktop Support during first term of CST-Networking
# Description: use a while loop to print count decided by user.

read -p "Enter a number to count to: " num

count=1
while [ $count -le $num ]; do 
       echo "$count"
       count=$(( count + 1 ))
done
echo "Done"
