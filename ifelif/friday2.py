import time

today = time.strftime("%A")# i have no clue what this does its OOP but i dont know the syntax yet i guess


print(today)
if today=="friday":
    print("Hell YEAH ITS FRIDAY")
else:
    print("fack Its not friday :((")
    

def times():#didnt work first 2 times 0 clue why now it does  
    a1 = time.strftime("%A")  
    a2 = time.strftime("%B")
    a3 = time.strftime("%Y")
    print(a2,a3,a1)
print(times())

