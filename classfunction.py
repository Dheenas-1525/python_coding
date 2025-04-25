#this code is using in class hour sample program :
def add(x,y):
	z=x+y
	print("result is : {} ".format(z))
	return z
a=int(input("enter the value of a :  "))
b=int(input("enter the value of b :  "))
print("value {} and {} is {} ".format(a,b, add(a,b)))
