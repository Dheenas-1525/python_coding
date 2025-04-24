#this code written by me fileopen in python
file_name = input("enter file name to be open\n")
f = open(file_name,'r')
print(f.read())
with open(file_name,'w') as file:
    file.write("this hello from the text of file after wriiten..!")
f.close()