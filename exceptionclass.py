#this code sibi bro worked in class video
import sys
a = 10
b = [1,2,3,4]
c = 5
#first one is use to try 
try:
    c = a + b[c]
except NameError as e:
    print("name error happend")
    print(e)