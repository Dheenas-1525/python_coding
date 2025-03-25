"""
first 256 number computer have static memory address.
don't use space in string
"""

#sring-imutable:
a="hello world"
print(a[2])

print(id(a))

a="hello world"
b="helloworld"
c="hello_world"
d="hello@world"
print(id(a))
print(id(b))
print(id(c))
print(id(d))

#during this above expriment string have memory address so it is called imutubale datatype.

#string concordination:

name="dheena"
msg=f"hi {name} welome to python programming {name}" #f means format this is used in all lasted python version 
print(msg)

#old versio of python string format:

msg="welcome to python programming {name}".format(name=name)
print(msg)

a="hello"
b="dheena"
c="welcome to python world"
print(a+" "+b+" "+c)

d="{host}"
print(a+"@"+d.format(host="google")+".com")
