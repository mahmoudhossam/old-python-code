def factorial(x):
	if x < 1:
		return 1
	else:
		return x * factorial(x-1)

def main():
	x = 1
	while x > 0:
		x = int(raw_input('enter a number: '))
		print 'The factorial for this number is %d' % (factorial(x))

if __name__ == "__main__":
	main()
