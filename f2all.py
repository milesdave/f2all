#!/bin/python

import getopt
import sys

try:
	opts, args = getopt.getopt(sys.argv[1:], "r")
except getopt.GetoptError:
	print("Usage: " + sys.argv[0])
	sys.exit(1)
