#!/usr/bin/python2

def start_count(end, begin = 1):
	for i in range(begin, end+1):
		print i
		
a = int(raw_input('Enter a number: '))

start_count(a)
