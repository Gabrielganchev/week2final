a=int(input())
b=int(input())
x=int(input())



def zad2(): # works 
    if x==a:
        print("then number is equal to the lower bound of the interl")
    elif x==b:
        print("the number is eqial to the upper bound of the interval")
    elif a<x<b:
        print("the number is in the interval")
    elif x<a:
        print("the number is outside the interval , x<a ")
    else:
        print("the number is outside the interval ,x>b")


print (zad2())
