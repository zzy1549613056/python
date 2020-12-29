#!/usr/bin/python

class Person(object):
	def __init__(self):
		self.__name = "private"
		self.__gender = None
		self.a = "ds"
		print "haha"

	@property
	def name(self):
		return self.__name

	@property
	def gender(self):
		return self.__gender

	def get_name(self):
		return self.__name

class Male(Person):
	def __init__(self,name):
		super(Male,self).__init__()
		print "Hello Mr." + name + self.name + super(Male,self).get_name() + self.a

class Female(Person):
	def __init__(self,name):
		print "Hello Miss." + name

class Factory:
	def getPerson(self,name,gender):
		if gender == "M":
			return Male(name)
		if gender == "F":
			return Female(name)


if __name__ == "__main__":
	factory = Factory()
	person = factory.getPerson("zzy","M")
