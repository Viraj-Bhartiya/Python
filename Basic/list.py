
# list aka array
x  = [1,2,3,4]

#to print length of list
print(len(x))

#to remove a element fron a list....removes the element not the element at that index
x.remove(2)
print(x)

#to insert a element in a list
x.insert(1,2)
print(x)

#pop removes the last element
print(x.pop())
print(x)

# delets the var
del x
#print(x)

#clears the elements of the list
x = [1,2,3,4]
x.clear()
print(x)

#sorts the list in ascending arder
x = [3,5,2,1,9]
print(x)
x.sort()
print(x)

#reverses the order of the list
x.reverse()
print(x)

#adds the valve at last
x.append(10)
print(x)

#copeis the list to other var
z = x.copy()
print(z)

#pritns the no os similar elements
z.append(10)
print(z.count(10))

#adds two lists
print(x+z)

#to print max value in a list
print(max(x))