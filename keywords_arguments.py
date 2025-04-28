"""this code shown the demo of how keywords and positional arguments worked in python"""
#varibales number in positional argumenst:
def add(x, *y):
    print(x)
    print(y)
    
    r = 0
    r = r + x
    for i in y:
        r = r + i
    return r
print("addition result : {}".format(add(1,2,3,4,5,6,7,8,9)))

def check(z, *v):
    print(z)
    print(v)
    g = z + v
    return g

print("result of g is : {}".format(add(23,1,3,4,5,6,7,8)))

#varibale number of keywords arguments
def keywords_args(a, j, l, **kwargs):
    # print()
    print(kwargs)
    return(kwargs)
keywords_args(1, 2, 3, h=1, b=2, c=3, d=4)


#varibale scopes:
x=5
def set_x(num):
    x=num
    print("hi this x from set_x : {}".format(x))    
    
def set_global_x(num):
    global x
    print(x)
    x=num
    print("hi this x from set_global_x : {}".format(x))
    
print(x)
set_x(50)
print(x)
set_global_x(76)
print(x)

    