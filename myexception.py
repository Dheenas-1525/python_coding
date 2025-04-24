#this code is my pov of exception handling:
a = 10
b = [1,2,3,4]
c = 5
try:
    c = a + b[2]
    # raise IOError("this is sample error...")
    print(c)
except IndexError as d:
    print("this is index error... : {}".format(d))
except NameError as d:
    print("this is name error : {}".format(d))
else:
    print("all going good")
finally:
    print("see the error good..")