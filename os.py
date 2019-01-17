# Get total size of directory
# Written by Lingzhi Zhang

import os	
from os.path import join, getsize, isdir

DIR = 4096 # size of empty directory


def getSize(dir):
	'''
		Get the size of the current dir and all the sub-dir
	'''
	total = 0
	dlist = os.listdir(dir) # list all the files or dir as a list 
	if dlist != []: # if dir is empty, skip
		for d in dlist:
			if isdir(join(dir,d)): # if elem in list is dir
				total += DIR # include the dir size 4096 bytes
				total += getSize(join(dir,d)) # use recursion to get the size of sub-dir
			else:
				total += getsize(join(dir,d)) # if elem is file, add to total

	return total


path = os.getcwd()
result = getSize(path)
print("Total size of current dir is: {} bytes.".format(result))