person1_name=input("enter the name\n")
person2_name=input("enter the name\n")
count=len(person1_name)+len(person2_name)
print(count)
flames=['friends','love','affection','marriage','enemies','sister']
print(flames)
while len(flames)>1:
	index=(count%len(flames))-1
	print(index)
	if index>=0:
		flames=flames[index+1:]+flames[:index]
	else:
		flames.pop()
print("status:",flames[0])
