from random import randint

a=int(input("enter dice side: "))
name_1=input("enter first player name: ")
name_2=input("enter second player name:")

name_1rls = randint(1,a)
name_2rls = randint(1,a)
if name_1rls>name_2rls:
    print (name_1 , "Has won, with a roll of %s" %name_1rls)
else:
    print (name_2 , "Has won , with a roll of %s"%name_2rls)
# i dont get how this will happen  with a function
