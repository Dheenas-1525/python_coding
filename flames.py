#wirte code for flames game...!
a="dheena"
b="dhayalan"
total_count=len(a)+len(b)
print(len(a))
print(len(b))
flames=['friends','love','affection','marriage','enimies','sister']
print(flames)
print(len(flames))
print(total_count)
while len(flames)>1:
	index=(total_count%len(flames))-1
	print(index)
	if index>=0:
		flames = flames[index+1:] + flames[:index]
		print(flames)
	else:
		flames.pop()
print("relationship status:",flames[0])
c="dheena"
print(len(c))
