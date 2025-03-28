#wirte code for flames game...!
a="dheena"
b="dhayalan"
total_count=len(a)+len(b) #see the total number string in  both a and b 
print(len(a))
print(len(b))
flames=['friends','love','affection','marriage','enimies','sister'] #set list index 0 to 6
print(flames)
print(len(flames))
print(total_count)
while len(flames)>1: #run the loop until iteration to get 1 value 
	index=(total_count%len(flames))-1 #calculate the index value from total_count and flames and using -1 
	print(index)
	if index>=0:
		flames = flames[index+1:] + flames[:index] #using slicing to pop and add before and after index value
		print(flames)
	else:
		flames.pop()
print("relationship status:",flames[0])

