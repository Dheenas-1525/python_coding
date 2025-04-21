#this is to test code of how string methods are used in python!
# first method is capitalize() it is used to upper case all first letter of sentence
txt="hello dheena welcome to this python world nice to meet you buddy.."
x=txt.capitalize()
print(x)

txt = "36 is my age."

x = txt.capitalize()

print (x) 

txt = "python is FUN!"

x = txt.capitalize()

print (x) 

#second one is casefold this method is used for to lowercase of string 
txt="DHEENA LOVE SUBRAJA"
x=txt.casefold()
print(x)

#third one is center fucntion its is used to algin the sentence in center

txt = "banana"

x = txt.center(20)

print(x)


txt = "banana"

x = txt.center(20, "O")

print(x) 


#fourth one is count is used to count the letters in the words

txt=" hi dheena how  are u "
text=txt.count("dheena")
print(text)


txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x) 


#fifth one is encode method
txt = "My name is Ståle"

x = txt.encode()

print(x) 

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
