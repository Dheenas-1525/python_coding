#this code used for to test and use case of python control structure!
#syntax of if-ellse statement..
"""
go the  shop(){
if(milkava()){
buy milk()
}
if(eggava()){
bug egg()
}
.......................
this above sudo code is if statement 
this is below sudo code is used for if-elif statement

if(milk ava())
{
bug milk()
}
elif(egg ava())
bug egg()
}
else()
{
dont bug anything
}
this is how sudo code works in python if else control statements.."""
#sample code:
#store=['milk','vegitables','eggs']
store=['vegitables']
if 'milk' in store:
	print("buy milk")
elif 'eggs' in store:
	print("bug eggs")
elif 'vegitables' in store:
	print("buy vegitables")
else:
	print("nothing is avaiable in store")

