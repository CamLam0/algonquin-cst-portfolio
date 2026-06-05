#!/bin/bash -u
# Note: Script derived from GNU/Linux Desktop Support lecture slides during first term of CST-Networking
# create 100 files with names filename1.txt thru filename100.txt ; don't touch any file that already exists

i=0
old=0
new=0

while [ $i -le 99 ]; do
	i=$(( i + 1 ))
	name="filename$i.txt"
	if [ -e "name" ]; then
		echo "Already created $name"
		old=$(( old + 1 ))
		continue
	elif ! touch "$name" ; then 
		echo 1>&2 "$0: Failed to create $name"
		break
	fi
new=$(( new + 1))
#i=$(( i + 1))
done
echo "Number of new files touched: $new out of $i"

