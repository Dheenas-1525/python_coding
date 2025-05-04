'''this code is showed how first class function is used python
this fucntion used to help multi funtion like function inside function'''
#syntax of this this function in python
def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_40 =create_adder(10)
print(add_40(100))
