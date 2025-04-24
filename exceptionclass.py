#this code sibi bro worked in class video
import sys
a = 10
b = [1,2,3,4,5]
c = 2
#first one is use to try 
try:
    c = a + b[c]
    raise IOError("this is sample error")
    print("value of c is {}".format(c))
except NameError as e:
    print("name error happend : {}".format(e))
    # print(e)
except IndexError as e:
    print("index error happend : {}".format(e))
    # print(e)
except Exception as e:
    print("something else : {}".format(e))
    print("error: {} ".format(+sys.exc_info()[0]))
else: 
    print("all good at this point")
finally:
    print("this will print always") 