#!/usr/bin/python2

def prime_candidates(x):
	odd = range(1, x, 2)
	odd.remove(1)
	return odd

def isprime(x):
	for i in range(2, x):
		if i % x == 0:
			return True
		else:
			return False

def main():
	counter = 0
	for i in prime_candidates(10000):
		if counter == 1000:
			break	
		elif isprime(i):
			counter += 1
			print i

if __name__ == '__main__':
	main()
