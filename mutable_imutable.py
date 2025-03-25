#below table is showed mutable and imutable datatypes....!
"""
int float string list tuple dictionary set
 I    I    I       M
"""
#datatypes memory management:
"""
mutubale and imutable is some core fundamentals concept of how memory is being mangement in python.

mutable once if it is assigned it can be modify with same address if you can modify the data stored in variable 
without modify address.it means that data type is mutable.

python don't have memory mangement don't worry about mangement.
"""
#example of mutubale and imutable:
a=1
b=1
print(id(a)) #same address of both a and b 
print(id(b))

a=2
b=a
print(id(a))
print(id(b)) #this is also remain same address

a=1
b=2
print(id(a))
print(id(b))


a=[1,2,3,4]

b=[1,2,3,4]

print(id(a))
print(id(b))

a=[1,2,3,4]
b=a
print(id(a))
print(id(b))

a=25678
b=25678
print(id(a))
print(id(b))
b=25678+1
print(id(a))
print(id(b))
