#this code is used in class videos
import sys
a = 10
b = [1,2,3,4]
c = 2

def divide(a,b):
    if b == 0:
        raise Exception("cannot divide by zero")
    return a+b
try:
    c = divide(5,b[5])
    raise Exception("chumma oru error")
    print("value of c is : {}".format(c))
except NameError as e:
    print("name error happend : {}".format(e))
    # print(e)
except IndexError as e:
    print("index error happend : {}".format(e))
    # print(e)
except Exception as e:
    print("something else : {}".format(e))
    print("error: {} ".format(sys.exc_info()))
else: 
    print("all good at this point")
finally:
    print("whatever the case is , i will work") 