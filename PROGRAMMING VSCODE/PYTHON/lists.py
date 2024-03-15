#lists are ordered,indexed and mutable sequences
#just like a tuple except,(changes allowed after creation),(object's position in list is fixed,
# (each object has a number for it's position)


#list element change
x=[1,2,2.3,'hello']
x[1] ='python'
print(x)
x[2]=500
print(x)

#list slices  : x[startindex:stopindex]

x=[1,3,3.56,'hello','python']
y=x[1:4]
print(y)
y=x[:3]
print(y)
y=x[2:]
print(y)
y=x[:]
print(y)

#constructors(creating new list)
x=list()
x=['a',25,'dog',8.43]
#list comprehension
x=[n for n in range(5)]
print(x)
x=[z**2 for z in range(10) if z>6]
print(x)

#list Append
x=[1,2,2.6,'hello']
x.append('python')
print(x)

#list insert
x=[1,2,2.6,'hello']
x.insert(2,1000)
print(x)

#list delete
x=[1,2,2.6,'hello']
del x[2]
print(x)

x=[1,2,2.6,'hello']
del x[1:3]
print(x)

#list remove
x=[1,2,2.6,2,'hello']
x.remove(2)
print(x)
x=[1,2,2.6,2,'hello']
x.remove('hello')
print(x)

#list pop
x=[1,2,2.6,'hello']
y=x.pop()              #display last object
print(y)
print(x)

x=[1,2,2.6,'hello']
y=x.pop(1)              #index 1
print(y)
print(x)

#list clear
x=[1,2,2.6,'hello']
x.clear()
print(x)

#list concatenation
x=[1,2,3]
y=[4,5,6]
z=x+y
print(z)
z=y+x
print(z)

#method 1
x=[1,2,3]
y=[4,5,6]
x.extend(y)
print(x)

#method 2 (for loop)
x=[1,2,3]
y=[4,5,6]
for z in y:
    x.append(z)
print(x)

#list reverse
x=[1,2,2.6,'hello']
x.reverse()
print(x)

#list sort             
x=[1,3,2,1,4]                    #lists must have the element of same type
x.sort()
print(x)

x=[1,3,2,1,4]
x.sort(reverse=True)
print(x)

x=[1,2,2,1,4]
x.sort(reverse=True)
print(x)

#Advance sort based on using key
#x.sort(reverse=True|False,key=myFunc)
x=['a','aaaaa','bb','bbb','cccc']
print(x)
def string_length(each_element):
    return len(each_element)
x.sort(key=string_length)
print(x)


x=[1,2,3,[10,100]]
print(x)
print(x[3])
print(x[3][0])     #within the inner list 
print(x[3][1])      


#lists copy
x=[1,2,3]
y=x.copy()
y.append(100)
print(y)
print(x)      #but x is not changed


#absolute value
a=list(map(abs,[-1,-2,0,1,2]))
print(a)



#QUIZ BASED ON LISTS

x=[1,2,3,4]
del x[:2]
print(x)

x=[1,2,3,4]   #pop removes the last element
y=x.pop()
print(x)
print(y)

x=['jupiter','earth','mars','io']
print(x[1][2])
print(x[-1][-1])

x=[1,2,3]
y=[1,2,3]
z1=x
z2=y[:]
z1[0]=999
z2[0]=999
print(x==z1)
print(y==z2)

