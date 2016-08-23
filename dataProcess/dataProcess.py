import re
import sys
import os


#sloppily strips html tags, and outputs data into a file 
def stripHTMLTags(infile, outfile):
	ifile = open(infile)
	ofile = open(outfile, 'w')

	fileText = ifile.read()

	fileText = re.sub('<[^>]+>', '', fileText)

	# fileText = re.sub('', '', fileText)

	ofile.write(fileText)
	ofile.close()

def generateClassArray(data):
	return

def generateWeaponArray(data):
	return

if __name__ == '__main__':
    print "filler"