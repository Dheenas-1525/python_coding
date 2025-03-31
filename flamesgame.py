a=input("enter first person name\n")
b=input("enter second person name\n")
count=len(a)+len(b)
flames=['friends','love','affections','marriage','enimeies','sister']
while len(flames)>1:
	index=(count%len(flames))-1
	if index>=1:
		flames=flames[index+1:]+flames[:index]
	else:
		flames.pop()
print("status:",flames[0])
