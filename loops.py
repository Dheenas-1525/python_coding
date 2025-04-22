'''this code is all about how loops working in python
there are two types of loops:
1)while loop
2)for loop(this loop is only used for structured program)
syntax of loop is ...
while<condition> this code will execute again and again until the 
condition become false and both have unique purpose 
the way of write code using loops :
1)intialize-var=10
2)condition-var<=10
3)update code-var=var-1
this while loop is used based on arthimatic condiotion '''
#syntax of while loop:
#var=10
#while var < 10 and var >= 0:
	#print("#{} hello world".format(var))
	#var=var-1
	#print("loop exited")
var = 10
while var <= 10 and var >= 0:
    print("#{} hello world".format(var))
    var = var - 1
print("loop exited")

a=10
b=20
while a == b:
	print("im from while")
	break
else:
	print("im from else")
while a != b:
	a=b
	if a ==b:
		print("im from if a value assigned to b")
		break
else:
	print("while block not working something went wrong....check the code..")
