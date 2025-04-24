file_name = input("enter a file name or path to read :")
f = open(file_name,'r')
i = 0
while i < 5:
    print(f.readline())
    i = i + 1
# print(f.read())
# f.close()


file_name = input("enter a file name or path to read :")
f = open(file_name,'r')
i = 0
line = f.readline()
while line:
    line = f.readline()
    print(line)
    #print(line, end="")
    #print(line.split(','))
    if i%5 == 0:
        output = input("read more line?[n]")
        if output == 'n':
            print("program exiting")
            break;
i = i + 1