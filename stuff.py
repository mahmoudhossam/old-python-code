##############################
# stuff.py 					 #
# a program that does stuff	 #
##############################

class stuff:
		
	def __init__( self, x=None, y=None):	
		self.x = x
		self.y = y
	
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def setX(self, i):
		self.x = i
	
	def setY(self, i):
		self.y = i

def main():
	s = stuff()
	s.setX(6)
	s.setY(4)
	print s.getX(), s.getY()

if __name__ == "__main__":
	main()
