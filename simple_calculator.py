#this code is to be create simple calculator using functons in python program
def calculator(x,y):
        add =x+y
        sub =x-y
        multi=x*y
        division=x/y
        return add, sub, multi, division

a = int(input("enter the value of  :  "))
b = int(input("enter the value of  :  "))

add, sub, multi, division = calculator(a,b)
print("basic maths result is  {} and {} ".format(a,b))
print("addtion of maths : {} ".format(add))
print("sub of maths : {} ".format(sub))
print("Multi of maths : {} ".format(multi))
print("division of maths : {} ".format(division))


try:
    with open("test.txt",'w') as file:
        # file.write("apo in try python only write str object ...")
        file.write("===============================================\n")
        file.write("this msg from try area in simple_calculator program")
        file.write("Basic maths result is {} and {}\n".format(a, b))
        file.write("Addition of maths: {}\n".format(add))
        file.write("Subtraction of maths: {}\n".format(sub))
        file.write("Multiplication of maths: {}\n".format(multi))
        file.write("Division of maths: {}\n".format(division))
        file.write("=====================================================")
except NameError as d:
    print("something else in try pls check that code ... {}".format(d))
else:
    print("code working fine........")