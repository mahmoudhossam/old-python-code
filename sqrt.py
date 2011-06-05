def getsqrt(x):
	l = 0
	while square(l) < x:
		l = 1 + l
	return l

def square(n):
	return pow(n, 2)

def	main():
	f = int(raw_input('Enter a number: '))
	print 'The square root of this number is', getsqrt(f)

if __name__ == "__main__":
	main()
