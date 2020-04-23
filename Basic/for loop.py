a = [0,1,2,3,4,5] # list
b = (0,1,2,3,4,5) #tuple
c = {0,1,2,3,4,6} #set
d = '012345'      #string
e = { #dictionary
    'name':'Viraj',
    'Age':15
}

#in operator
#in gives values t/f 

print(0 in a)
print(1 in b)
print(2 in c)
print('3' in d)

for x in a :  #can b tried with b,c,d
    print(x)

#for loop for dictionary

for x in e.keys(): #can b used with .values() , .items()
    print(x)

for key,value in e.items() :
    print(key,' ',value)

for x in range(10):  #for(int x = 0;x<10;x++)
    print(x)

for x in range(1,10): #for(int x = 1;x<10;x++)
    print(x)

for x in range(1,10,2): #for(int x = 1;x < 10; x+=2)
    print(x)
else :
    print(" Loop Finished")