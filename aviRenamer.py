#!/usr/bin/python

import sys, os

verbose = False
lista = []
if os.path.isfile(sys.argv[2]): ficheiro=sys.argv[2] 
else: sys.exit("ERROR :: File not found!")

if (len(sys.argv) > 2) and (sys.argv[1] == '-v'): verbose = True

f = open(ficheiro, 'r')
path="."
dirList=os.listdir(path)

for fname in sorted(dirList):
    basename, extension = os.path.splitext(fname)
    if (extension == '.avi'):
    	lista.append(fname)

for i,line in enumerate(f):
	line = line.strip()
	os.rename(lista[j], line)
	if verbose : print lista[i], "renamed to", line

f.close()
