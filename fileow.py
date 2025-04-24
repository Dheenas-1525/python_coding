#this is my own code practice for file write and open
file_name = input("enter the file name:\n")
f= open(file_name,'r')
print(f.read())
with open(file_name,'w') as file:
    file.write("this msg from file.write buddy...")
    # print(file.write())
