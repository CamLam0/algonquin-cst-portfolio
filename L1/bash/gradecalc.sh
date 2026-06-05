#!/bin/bash
# Note: Script derived from GNU/Linux Desktop Support lecture slides during first CST-Networking semester.
# Description: this script will calculate a final grade for a semester with six courses and error checking.

if [ $# -ne 6 ]; then
	echo "You have entered grades for $# subjects."
	echo "Please enter marks for all six subject."
	exit
fi

p=$((($1+$2+$3+$4+$5+$6) / 6))

echo "Your average grade percentage this semester is $p"

if [ $p -ge 90 ] ; then 
	echo "Your average is A+"
else 
	if [ $p -ge 80 -a $p -le 89 ] ; then
		echo "Your average is A"
	else
		if [ $p -ge 70 -a $p -le 79 ] ; then
			echo "Your average is B+"
		else	
			if [ $p -ge 60 -a $p -le 69 ] ; then
				echo "Your average is B"
			else				
				if [ $p -ge 50 -a $p -le 59 ] ; then
					echo "Your average is C"
				else
					if [ $p -lt 50 ]; then 
						echo "Your average is F"
					fi
				fi
			fi
		fi
	fi
fi

