#!/bin/bash -u
# Name: break3-backup.sh
# Note: Derived from GNU/Linux Desktop Support slides during my first CST-Networking semester
# Description: Make backup copies of file names given as arguments; Stop copying if any error occurs.

count=0
for file do 
	if ! cp -p "$file" "$file.backup" ; then
		echo 1>&2 "$0: Failed to copy '$file' to '$file.backup'"
		break
	fi
	count=$(( count + 1 ))
done
echo "Number of files backed up: $count of $#"
