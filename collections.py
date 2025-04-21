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
l[1]='replaced word'
print(l)
n=[1,2,3,4,5]
k=[6,7,8,9,10]
print(n+k)
'''secong is tuple is sames as list but tuple is used brackets instead of using square brackets and also consider tuple is consider as immutable datatype
so there is not avaiable of curd fucntions like pop delete and append in tuple and also create tuple for single using common after values because python is strongly connected with bodmass rule '''
#syntax of tuple is :
t=tuple()
print(t)
t=('dheena','dhayalan','sub','raja')
print(t)
#t[1]="dhayalanaa"
#print(t) this is the example tuple cant changes the values so its called as immutable 
#there is function is packing and unpacking in python!
"""next one is dictionay in collections """
#syntax in dict is:
d={'name':'dheena','age':'25','country':'india'}
print(type(d))
print(d)
c={}
print(c)

thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 2022,
  "year": 2020,
  "name":'dheena'
}
print(thisdict)
#so next one is set  is also sames as dictionary but duplicate not possible 
#syntax
es=set()
print(es)
es={1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9}
print(es)
es={1,3,4,5,6,}
es1={9,8,7,5,3,}
print(es & es1)
print(es | es1)
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset)) 

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 

print(set1)
print(set2)
print(set3)


set1 = {"abc", 34, True, 40, "male"}
print(set1)
