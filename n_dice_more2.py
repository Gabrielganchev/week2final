#dice roll
from random import randint
c=int(input("please insert a number"))
b=0
while b<=2:
    a=randint(1,c)
    print("the dice roll is -->",a ) 
    b+=1
    
    
