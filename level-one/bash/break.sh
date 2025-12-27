#!/bin/bash -u
# Name: break.sh
# Description: this script is derived from GNU/Linux lecture slides
# It is included here to demonstrate the difference between break and continue statements

count=0
for value do 
	(( count += 1 ))

	if [ "$value" = "tim" ] ; then
		echo "########################################"
		echo "NOTE: "
		echo "Please dont use this value = $value"
		echo "Invalid argument is at number $count"
		echo "########################################"
#	break
 continue
	fi
	echo ""
	echo " The #$count argument passed is --> $value"
done
echo ""
echo " Total number of arguments passed is $#"

