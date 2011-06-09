#!/usr/bin/python2
class cls:
	def __str__(self):
		return "this is %s" % (__name__)
instance = cls()
print instance
