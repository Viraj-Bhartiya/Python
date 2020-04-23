a = {'name':'Viraj','year':20,'age':15}
print(a)
print(a['name'])

print(a.get('year'))
print(len(a))

a['Surname'] = 'Bhartiya'
print(a.get('Surname'))

a.pop('Surname')
print(a)

a['name'] = 'Citrus'
print(a['name'])

a.update({'name':'Viraj'})
print(a['name'])

print(a.keys())

#removes last item
a.popitem()
print(a)

a.clear()
print(a)

del a
#you can store any kind of values