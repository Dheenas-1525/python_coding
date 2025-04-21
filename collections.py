#this code fully test for python collections 
"""
there are four type of collections avaliable in python
1)list
2)tuple
3)dictionary
4)set
there are collections in python"""

#first one is list  list is consider as mutable datatype  we can change the values in list .
"""
syntax of list is 
l=list[]
"""
l=['dheena','dhayalan','dheena','subraja','sridhar']
for i in range(0,len(l)):
	print("id->{},word of ->{}".format(id(l),l[i]))

print(id(l))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#slicing in the list 
"""
slicing is a function that is accessing the index of the given  values """

print(l[1:5])
print(l.pop(0))
print(l)


l.append('karthi')
print(l)


'''
slicing alter version is copy() function in python it is called rapper fucntion  copy function is used duplicate the
the object'''
a=l.copy()
print(a)
print(id(l))
print(id(a))
a[4]='subdhee'
print(a)
print(l)
l[4]='dheesubhu'
print(l)
print(a)
l=a
print(a)
l[4]='this is changed one'
print(l)
print(a)

#in keywords in python 
if l[1] in ['dheena']:
	print("true")
else:
	print("false")

print(l)
'''secong is tuple is sames as list but tuple is used brackets instead of using square brackets and also consider tuple is consider as immutable datatype
so there is not avaiable of curd fucntions like pop delete and append in tuple and also create tuple for single using common after values because python is strongly connected with bodmass rule '''
#syntax of tuple is :
t=tuple()
print(t)
