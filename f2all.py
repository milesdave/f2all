#!/bin/python

import getopt
import glob
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

# number of zeroes to pad file number with
pad = 0

# glob pattern
pattern = ""

# get cmd opts/args
try:
	opts, args = getopt.getopt(sys.argv[1:], "rd:b:s:z:g:")
except getopt.GetoptError:
	print("Usage: f2all [-r] [-d directory] [-b base-name] [-s start-num]\n"
		"             [-z pad-num] [-g pattern]\n\n"
		"  -r                    perform the renaming\n"
		"  -d directory          directory of files to rename\n"
		"  -b base-name          base name for all files to use\n"
		"  -s start-num          starting file number\n"
		"  -z pad-num            number of zeroes to pad file number with\n"
		"  -g pattern            glob pattern for file matching")
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
	# zero padding argument
	elif opt in "-z":
		pad = int(arg)
	# glob argument
	elif opt in "-g":
		pattern = arg

# make sure directory ends with a '/'
if not filedir.endswith('/'):
	filedir += '/'

filelist = os.listdir(filedir) if not pattern else glob.glob(filedir + pattern)
filelist.sort()

for filename in filelist:
	# build new file name
	ext = os.path.splitext(filename)[1]
	newname = base + str(num).zfill(pad) + ext

	# remove path from glob output
	if pattern:
		filename = filename.split('/')[-1]

	print(filename + " -> " + newname)

	# actually rename if -r set
	if rename:
		os.rename(filedir + filename, filedir + newname)

	num += 1
