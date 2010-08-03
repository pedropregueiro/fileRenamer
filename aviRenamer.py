#!/usr/bin/python

import sys, os, glob, getopt

verbose = False
renamer = False
dry = True
list = []
ficheiros = []

options, args = getopt.getopt(sys.argv[1:], 'rv', ['verbose','rename'])
file = args[0];

if not os.path.isfile(file):
	sys.exit("ERROR :: File not found!")
														 
for opt, arg in options:
	if opt in ('-v', '--verbose'):
		verbose = True
	if opt in ('-r','--rename'):
		renamer = True
	else:
		dry = False

f = open(file, 'r')

for line in f:
	ficheiros.append(line.strip())
	
if (len(glob.glob('*.avi')) != len(ficheiros)):
	exitErr = 'ERROR :: Number of .avi files and number of lines in ' + file + ' not equal!'
	sys.exit(exitErr)


list = sorted(glob.glob('*.avi'))

for i,line in enumerate(ficheiros):
	if renamer:
		if verbose: 
			print list[i], "renamed to", line
		os.rename(list[i], line)
	else:
		print list[i], " --> ", line

f.close()