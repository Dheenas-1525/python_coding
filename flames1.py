#logic of flames 
name1=input("enter name1\n")
name2=input("enter name2\n")
count=len(name1)+len(name2)
print("number of words in both name:",count)
flames=['friends','love','affection','marriage','enemies','sister']
while len(flames)>1:
	index=(count%len(flames))-1
	if index>=0:
		flames = flames[index+1:] + flames[:index]
	else:
		flames.pop()
print("relationship with ur partner is:",flames[0])
