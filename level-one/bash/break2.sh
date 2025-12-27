#!/bin/bash -u 
# Name: break2.sh
# Description: Taken from GNU/Linux slides to better understand the difference between 'break' and 'break 2'
# Uncomment either below to see the effects when executing this script.

dow=1
week=1
while [ $week -le 52 ]
	do
		while [ $dow -le 7 ]
		do
			echo "Week $week, Day $dow"
			(( dow += 1 )) #increment by 1 or dow=$(( dow + 1 ))
			#break will exit the inner loop
			# uncomment break and test the script
		#	break
			# break 2 will exit two levels of nested while loops
		#	break 2
		done
	dow=1
	(( week += 1 )) # increment by 1
done 
echo ""
