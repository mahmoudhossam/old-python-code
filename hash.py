#!/usr/bin/python2
from hashlib import md5
from sys import argv
'''md5 hash calculator.

Calculates md5 hash sum for a given file.'''
def sum(x):
	f = open(x, 'r')
	digest = md5()
	digest.update(f.read())
	f.close()
	return digest.hexdigest()

def main():
	if len(argv) < 2:
		print "Usage: \"hash file\""
	elif len(argv) == 2:
		print sum(argv[1])
	else: print "only 1 argument allowed, %d given" % (len(argv))

if __name__ == "__main__":
	main()
