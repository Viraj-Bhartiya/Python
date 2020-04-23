#removes the duplicate values

x = {1,2,3,5,9,2,4,2,3,4}
print(x)

x.add(10)
print(x)

x.update({15,2,5,11,4,45,2,})
print(x)

x.remove(15)
print(x)

x.discard(11)
print(x)

#removes any random element
x.pop()
print(x)

x.clear()
print(x)

#del x

z = set((2,12,323,21,21,21,11,2,121,2,1))
print(z)

#converts list to set
#z = {[1,2,3,4]}
#print(z)

#union of 2 sets
print(x | z)
x.union(z)
print(x)

#prints similar elements of a set
x.intersection(z)
print(x & z)

#prints values which are different
print(x-z)
x.difference(z)
print(z-x)

#prints symetric difference
print(x ^ z)
print(x.symmetric_difference(z))

#sets are not indexed