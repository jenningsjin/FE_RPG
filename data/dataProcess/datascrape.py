import re
import sys
import os



def processData(argv):
	ifile = open(argv[1])
	ofile = open("outdata.txt", 'w')

	fileText = ifile.read()

	fileText = re.sub('<[^>]+>', '', fileText)

	# fileText = re.sub('', '', fileText)

	ofile.write(fileText)
	ofile.close()

if __name__ == '__main__':
    processData(sys.argv)
    