#!/usr/bin/python

import sys, os, glob, getopt

verbose = False
renamer = False
files = []
oldFiles = []

options, args = getopt.getopt(sys.argv[1:], 'rve:', ['extension=','verbose','rename'])														 
for opt, arg in options:
	if opt in ('-v', '--verbose'):
		verbose = True
	if opt in ('-r','--rename'):
		renamer = True
	if opt in ('-e', '--extension'):
		if arg.startswith('.'):
			ext = '*'+arg
		else:
			ext = '*.'+arg
		
file = args[0]
if not os.path.isfile(file):
	sys.exit("\nERROR :: File not found!\n")
f = open(file, 'r')

for line in f:
	dotArray = line.strip().split(".")
	if (dotArray[len(dotArray)-1] == ext.replace('*.','')) and (line != file):
		files.append(line.strip())

for elem in glob.glob(ext):
	if elem != file:
		oldFiles.append(elem)

if len(oldFiles) == 0:
	sys.exit('\nWARNING :: No files with extension ' + ext + ' in ' + os.path.abspath('.') + '\n')
		
if (len(oldFiles) != len(files)):
	exitErr = '\nERROR :: Number of ' + ext + ' files ('+ str(len(oldFiles)) + ') and number of lines (' + str(len(files)) + ') in ' + file + ' not equal!\n'
	sys.exit(exitErr)

oldFiles = sorted(oldFiles)
for i,line in enumerate(files):
	if renamer:
		if verbose: 
			print oldFiles[i], "renamed to", line
		os.rename(oldFiles[i], line)
	else:
		print oldFiles[i], " --> ", line
		
f.close()