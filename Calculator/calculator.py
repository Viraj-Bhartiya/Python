def add(a,b): 
    return(a+b)

def sub(a,b):
    return (a-b)

def mult(a,b):
    return (a*b)

def div(a,b):
    return (a/b)
print("Menu : \n1. add\n2.sub\n3.mult\n4.div")

n = int(input("Enter your choice 1\2\3\4 "))

x = int(input("enter arg. 1 "))
y = int(input("enter arg 2 "))

if n == 1:
    print(add(x,y))
elif n == 2:
    print(sub(x,y))
elif n == 3:
   print(mult(x,y))
elif n == 4:
    print(div(x,y))
