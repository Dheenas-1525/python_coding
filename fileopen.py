'''this code use to practice how file opens and filewrite works in python'''

file_name = input("enter a file name or path to read :")
f = open(file_name,'r')
print(f.read())
f.close()