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
	print("result is : {} ".format(z))
	return z
x=int(input("enter the value : "))
y=int(input("enter the value : "))
print("value {} and {} is {} ".format (x,y, add(x,y)))



def portflio(name, age, address):
    d = {
        "name": name,
        "age": age,
        "address": address
    }
    print(d)
    return d

a = 'dheena'
b = 25
c = 'koradacheri'
print(a, b, c, portflio(a, b, c))





def portflio(name, age, address)
	d = {
	     "name": name,
             "age": age,
             "address": address
	     }
	     print(d)
	     return d
user1 = input("enter your  name age address"
