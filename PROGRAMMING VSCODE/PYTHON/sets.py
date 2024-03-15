#sets are unordered and non-duplicate collection
#sets are mutable

#set creation
x={'red','green','yellow'}
print(type(x))
y={1,2,2,4,3,3}     #duplicate values are removed in sets
print(y)

#'in'Keyword
x={'red','green','yellow'}
y={1,2,4,3}
print('red' in x)
print('brown' in x)
print(1 in y)
print(7 in y)

#set access
x={'red','green','yellow'}          #no guarantee of order
for e in x:
    print(e)

#set addition
x={'red','green','yellow'} 
x.add('brown')
print(x)

x={'red','green','yellow'}             #use x.update to add multiple objects 
x.update(['brown','orange','purple'])
print(x)

x={'red','green','yellow'}  
x.update('blue')
print(x)



#element removal
x={'red','green','yellow'}         #error if item not found
x.remove('green')
print(x)

x={'red','green','yellow'}         #No error if item not found   
x.discard('black')
print(x)

#set clear and delete
x={'red','green','yellow'}
x.clear()
print(x)

#set copy
x={'red','green','yellow'}  
y=x.copy()
print(y)
print(id(x))
print(id(y))

#set unions
x={1,2,3}
y={4,3,2}
z={4,6,5}
a=x.union(y,z)                 #returns a new set
print(a)

x={1,2,3}
y={4,3,2}
z={4,6,5}
x.update(y,z)                   #updates old set
print(x)


#set intersection & difference
x={1,2,3}
y={4,3,2}
z=x.intersection(y)
print(z)                        #only common elements

x={1,2,3}
y={4,3,2}
z=x.difference(y)
print(z)

x={1,2,3}
y={4,3,2}
w=y.difference(x)
print(w)

#frozen set
x={1,2,3}                   #cannot add or delete elements
y=frozenset(x)              #frozen set is hashable as it is immutable
print(y)


#QUIZ

x={1,'a',2,'b'}
y={'a','c',3,4}
print(x.difference(y))
print(y.difference(x))

x={1,2,3}
y={1,2,3,4,5,6}
print(x.issubset(y))
print(y.issubset(x))

print(x.issuperset(y))
print(y.issuperset(x))
