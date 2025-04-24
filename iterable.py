'''iterables
there are two type if iterable 
1)iter:make an iterator out of an iterable datatype
2)gives the next in list
'''
l = [1,2,3,4,5,6,7,8,9,10]
d = {"a": "b", "c": "d", "e":"f"}
for i in iter(d):
    print(i)
    
l = iter(l)

print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))