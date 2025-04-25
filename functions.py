'''it is group of instruction given to a computer to do a meaningfull task
'*' use def to create a new function def is a keyword:
'*' def is keywords and add is a fucntion(a,b) is variables or positional aruguments
#syntax of fucntion:
def add(a,b)
	c=a+b
	print("result is : {}".format(c))
	return c
this is the  syntax of function in python programming'''

#practice code for python:
def add(a,b): #this is my first function program in python
	z=a+b
	return z
x=int(input("enter the value : {}".format(x)))
y=int(input("enter the value : {}".format(y)))
print("value {} and {} is {} ".format (x,y, add(a,b)))

