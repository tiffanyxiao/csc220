
'''
Objective: write a program that reads all the python files in a specified directory
and prints out the number of lines of code in each (ignoring whitespace and
comments)
'''
import glob, os

import collections

list0 = []

path = "/Users/karensantamaria/Documents/School Past/Spring 17/CSC 111/All Graphics/*.py"
for filename in glob.glob(path):
	with open(filename, 'r') as f:
		mytest = [x for x in f if( (x.strip()) and (not x.strip().startswith("#"))) ]



		print(len(list0))







    