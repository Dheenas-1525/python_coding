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
	if a == b:
		print("im from if a value assigned to b")
		break
else:
	print("while block not working something went wrong....check the code..")

name = input("enter your name\n")
while len(name) == 10:
	print("welcome! to this magic world {name}".format(name=name))
	break
else:
	print("Enter your name with in ten characters")
'''Next one is for loop for is iteraable and structured one using in python'''
# for i in range(0,1000):
# 	print(i)
 
name1=input("enter your name\n")
for i in range(len(name1)):
	print("#{},words {}".format(i,name1[i]))
print(i)

f=['dheena','karthi','arun','senthil']
print(f[0])
print(f[1])
for i in range(len(f)):
	# print(i)
	print("#{} name:{}".format(i, f[i]))
	# print("#{}".format(i,f[i]))

# name2=input("enter ur name")
# for i in range(0,10):
#     print(name2)
names=[]
for i in range(10):
    name=input("enter name{}: ".format(i+1))
    names.append(name)
print("list of Names...!")
for i in range(10):
    print("index {}: {}".format(i,names[i]))

l=['apple','orange','mongo']
for v in l:
    print(v)

'''next using break statements loops in python'''
for d in range(0,100):
    print(d)
    if d>60:
        break
print("loop exited")

for c in range(10,100):
    if c % 2 == 0:
        continue
    else:
        print(c)
print("this print in from odd number")

g=['dheena','subraja','arun']
for i in list(g):
    if i == 'arun':
        continue
    else:
        print(i)

'''pending to workout is break and contionue and enumeration....next will see exception handling and file handling
exception handling to see try exception else and finally
file handling  homework try to write files..
'''

"""thats all about the loops"""

'''enumeration is also like that dictionary like that
packing and unpacking method like giving or assign the index of
values'''

#syntx of enumeration :
em=['a','b','c']
for i in enumerate(em):
	print("#{} {}".format(i,i))


