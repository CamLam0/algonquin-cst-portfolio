#!/bin/bash
# Note: Derived from GNU/Linux Desktop Support lecture slides during my first term in CST-Networking
# Description: This script creates a menu using two defined functions to reveal system information.

function DISTRO() {
	DISTROS=$(hostnamectl | grep Operating | awk '{print $3,$5}')
	echo " POS Distro is: " $DISTROS
}

function system_info() {
	ip=$(ifconfig | grep inet | head -1 | awk '{print $2}')
	MAC=$(ifconfig | grep ether | head -1 | awk '{print $2}')
	echo "IP Address is $ip"
	echo "MAC Address is $MAC"
}

clear

while [ TRUE ]; do 
	read -p "OS (I)nfo , (S)ystem Info , (C)lear, (D)ate , (Q)uit " INPUT
	case $INPUT in
		I|i)
			echo "Info about OS"
			DISTRO
			;;
		S|s) 
			echo "System Information"
			system_info
			;;
		Q|q)
			echo "Quitting..."
			break
			;;
		C|c)
			clear
			;;
		D|d)
			echo "Today's date and time: "
			date
			;;
		*)
			echo "Wrong input. Try again."
			;;
	esac
done
