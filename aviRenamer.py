#!/usr/bin/python

import sys, os, glob

verbose = False
lista = []
if os.path.isfile(sys.argv[2]): ficheiro=sys.argv[2] 
else: sys.exit("ERROR :: File not found!")

if (len(sys.argv) > 2) and (sys.argv[1] == '-v'): verbose = True

f = open(ficheiro, 'r')

for item in glob.glob('*.avi'):
	lista.append(item)

for i,line in enumerate(f):
	line = line.strip()
	os.rename(lista[i], line)
	if verbose : print lista[i], "renamed to", line

f.close()
