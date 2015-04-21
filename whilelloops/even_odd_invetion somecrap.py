a=int(input("lower number"))
b=int(input("higher number"))


while a<=b:
    
    a+=1
    if a%2==0:
        print(a,"- even")
    elif a%2==1:
        print(a,"- Odd")
        
