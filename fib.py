#!/usr/bin/python

def fib(x):
	if x == 0 or x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)
def main():
	x = int(raw_input('enter number: '))
	print fib(x)

if __name__ == '__main__':
	main()
