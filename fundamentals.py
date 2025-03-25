#hello world!
print("hello wolrd")
#primitive_datatypes....!
a=2
b=3
print(a+b) #addition
print(a-b) #sub
print(a*b) #multi
print(a/b) #divide
print(a//b) #intiger divide
print(a%b) #modulo
print(a**b) # exponent

#bodmas_rule
print((a+b**2+(a+b)**2)/2)

#booleans:
print(True) #always Capital t case sensitive
print(False) #also like above 
print(True+False) 
print(False+False)

#comparision_operators:
a=10
b=20
print(a is  b)
print(a==b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a!=b) #these above all are the comparison operators 


#chaining_comparision(applicable in if-else statement)
"""
there are  lots of chaning compaprision operators but basic main fundamentals is three only that is 
AND OR NOT """

# this is and comparision
"""
a b r
0 0 0
0 1 0
1 0 0
1 1 1

this is table of and gate"""

print(10>=100 & 100>=200) # this statement is  0+0=0 so output is false 
print(10>=100 & 100<=200) # this statement is  0+1=0 so output is false 
print(10<-100 & 100>=200) # this statement is  1+0=1 so output is False 
print(10<=100 & 100<=200) # this statement is  1+1=1 so output is True

#specific fuction of python:
""" 
is-> checks if both var have same refrence

id-> location value it is stored each &every varibale that you decleared as an address"""

a=2
b=5
print(a is b)
print(id(a))
print(id(b))


