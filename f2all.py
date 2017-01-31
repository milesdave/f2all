#!/bin/python

import getopt
import os
import sys

# only rename if -r specified
rename = False

# directory of files to rename - cwd by default
filedir = os.getcwd()

# get cmd opts/args
try:
	opts, args = getopt.getopt(sys.argv[1:], "rd:")
except getopt.GetoptError:
	print("Usage: " + sys.argv[0] +
		" [-r] [-d directory]")
	sys.exit(1)

# parse opts/args
for opt, arg in opts:

	# rename flag
	if opt in "-r":
		rename = True
		print("raname = True")

	# directory flag
	elif opt in "-d":
		filedir = arg
		print("filedir = " + filedir)
