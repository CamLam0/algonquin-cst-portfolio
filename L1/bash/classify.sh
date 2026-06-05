#!/bin/bash
# Name: classify.sh
# Note: Derived from GNU/Linux Desktop Support slides during my first semester of CST-Networking
# Description: Classify a positional parameter given by the user with a CASE block

case "$1" in 
	"dog" | "cat" | "goat" | "pig" )
		kind='animal'
		;;
	"apple" | "peach" | "plum" | "cherry" )
		kind='fruit'
		;;
	* ) 
		kind='unknown'
		;;
esac
echo "$1 is a $kind"

