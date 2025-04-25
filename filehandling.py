try:
	f=open("hello.txt",'r')
	print(f.read())
	with open("hello.txt",'w') as f:
		f.write("this is from another world hello machi how r u ...")
		#print(f.write())
except NameError as v:
	print("something else in file name check file name correctly first...! ; {}".format(v))
else:
	print("program run smoothly...")
	f.close()
