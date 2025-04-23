'''this code is look at exception handling it is used to through errors not in code error it totally outside error
like if download file from internet if internet disconnected it show connect the your network like that of error 
there are four type of errror 
1)try
2)exception
3)else
4)finally these are that four types exception handling in python '''

#first one is try:
a=10
b=20
# try:
#     if(a == b):
#         print("hi im from try it working succesfully..")
# except:
#     print("something wrong...!")
try:
    result = a / 0   # Division by zero causes an error
    print(result)
except:
    print("something wrong...!")  # This will run

finally:
    print("this print wll show output anyway if error occur or error...")
