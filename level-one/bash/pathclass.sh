#!/bin/bash -u
# Note: Script derived from GNU/Linux Desktop Support lecture slides during first term of CST-Networking
# Description: this script will classify a pathname passed as a positional parameter

case "$1" in 
	'' ) type="missing (empty)" ;;
	/* ) type="Absolute pathname" ;;
	*/ ) type="Relative pathname ending with a slash" ;;
	*/* ) type="Relative pathname in some directory" ;;
	*' '* ) type="Relative pathname with blank(s)" ;;
	* ) type="Relative pathname in current directory" ;; # default
esac
echo "Pathname '$1' is $type"

