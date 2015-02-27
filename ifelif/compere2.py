a=int(input("number :"))
b=int(input("number : "))
def largest_from_2(a,b):#works same as the video nothing fancy there 
    largest = a
    if b>=a:
        largest = b
    if a>=b :
        largest = a
    return largest
