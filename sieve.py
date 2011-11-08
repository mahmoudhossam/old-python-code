#!/usr/bin/python2

from math import *

def prime_candidates(x):
	odd = range(1, x, 2)
	odd.insert(0, 2)
	odd.remove(1)
	return odd

def isprime(x):
	for i in range(2, int(sqrt(x) + 1)):
		if x % i == 0:
			return False
	else:
		return True		

def add(x, y):
	return x + y
	

def main():
	end = 8000
	candidates = prime_candidates(end)
	primes = filter(isprime, candidates)
	primes = primes[:1000]
	sum_of_logs = reduce(add, map(log, primes))
	print 'sum is: ' + str(sum_of_logs)
	print 'ratio is: ' + str(primes[len(primes) - 1] / sum_of_logs)
			
if __name__ == '__main__':
	main()
