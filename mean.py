import sys

def mean(nums):
	result = 0
	for i in nums:
		result += i
	return result / len(nums) 

def main():
	list = []
	while True:
		i = int(raw_input('enter a number: '))
		if i > 0 :
			list.append(i)
			print 'you entered %s' % (str(list))
		elif i == 0 :
			print mean(list)
			list[:] = []
		else: sys.exit()

if __name__ == '__main__' :
	main()
