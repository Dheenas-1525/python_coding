#this code is shown about how varibale scopes works in pythonnlike global and local varibale
x=5
def set_local_x(num):
    x=num
    print("this is from set_local x : {}".format(x))

def set_global_x(num):
    global x
    print("this is from global x : {}".format(x))    
    x = num
    print("this x global but its output is local : {}".format(x))
    
set_local_x(50)
#print("this x from set_local_x : {} ".format(x))
print(x)
print(x)
set_global_x(55)
#print("this x from set_global_x : {}".format(x))
print(x)
print(x)



