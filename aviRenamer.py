#!/usr/bin/python

import re, string, sys, os;


#
# opcao -v  => verbose:    change.py -v file.txt == file1.avi renamed to ficheiro1.avi
#

verbose = False;


if (len(sys.argv) > 2) and (sys.argv[1] == '-v') : verbose = True;


f = open('troca.txt', 'r')

i = 0

#for line in f:
#	if(line!='\n'):
#		print line,
	
#	i+=1;
	

path="."
dirList=os.listdir(path)

for fname in dirList:
	basename, extension = os.path.splitext(fname)
	if (extension == '.avi'):
		print basename;
		
	for line in f:
			print line;
			
	
		
	
	
		


		


f.close();	


#if verbose : print "hello world: " + sys.argv[2]; 
