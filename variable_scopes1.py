x=10
def set_local_x(num):
    x = num
    print(x)

def set_global_x(num):
    global x
    print("hi this x from the global : {}".format(x))
    x=num
    print(x)

set_local_x(20)
print(x)
set_global_x
print(x)
