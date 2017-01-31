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
		" [-r] [-d directory] [-b base-name] [-s start-num]\n\n"
		"  -r                    perform the renaming\n"
		"  -d directory          directory of files to rename\n"
		"  -b base-name          base name for all files to use\n"
		"  -s start-num          starting file number")
	sys.exit(1)

for opt, arg in opts:
	# rename flag
	if opt in "-r":
		rename = True
	# directory argument
	elif opt in "-d":
		filedir = arg
	# base name argument
	elif opt in "-b":
		base = arg
	# starting number argument
	elif opt in "-s":
		num = int(arg)

filelist = os.listdir(filedir)
filelist.sort()

for filename in filelist:
	#build new file name
	ext = os.path.splitext(filename)[1]
	newname = base + str(num) + ext

	print(filename + " -> " + newname)

	# actually rename if -r set
	if rename:
		os.rename(filedir + filename, filedir + newname)

	num += 1
