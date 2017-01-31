#!/bin/python

import getopt
import os
import sys

# only rename if -r specified
rename = False

# directory of files to rename - cwd by default
filedir = os.getcwd()

# base file name
base = ""

# file number
num = 1

# get cmd opts/args
try:
	opts, args = getopt.getopt(sys.argv[1:], "rd:b:s:")
except getopt.GetoptError:
	print("Usage: " + sys.argv[0] +
		" [-r] [-d directory] [-b base-name] [-s start-num]")
	sys.exit(1)

# parse opts/args
for opt, arg in opts:
	# rename flag
	if opt in "-r":
		rename = True
		print("raname = True")
	# directory argument
	elif opt in "-d":
		filedir = arg
		print("filedir = " + filedir)
	# base name argument
	elif opt in "-b":
		base = arg
		print("base = " + base)
	# starting number argument
	elif opt in "-s":
		num = int(arg)
		print("num = " + str(num))
