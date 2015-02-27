a=int(input("number for first user"))
b=int(input("number for second user"))


oper = input("operatin: ")
def operation(oper):#works but i feel like idiot
    if oper=="+":
        return a+b
    elif oper=="-":
        return a-b
    elif oper=="*":
        return a*b
    elif oper=="/":
        return a/b
print(operation(oper))



    
