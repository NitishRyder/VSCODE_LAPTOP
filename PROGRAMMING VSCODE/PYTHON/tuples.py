my_tuple = (1,2,3)                #declared cannot be changed
print(my_tuple[2])

a=()
b=(1,)
c=(1,2.3)
d=(1,2.3,'hello')
e=1,2.3,'hello'
type(a)
type(b)
type(c)
type(d)
type(e)
print(type(a),type(b),type(c),type(d),type(e))


#tuple packing
a=1
b=2.3
c='hello'
x=(a,b,c)
print(x)

#unpacking a tuple
a=(1,2,3)
x,y,z=a
print(x,y,z)

a=(1,2,3)
_,y,_=a
print(y)

#in operator
x=1,3,'hello',2.3,'5.4'
a=1 in x
b=5 in x
c='hello' in x
d=5.4 in x
e='5.4' in x
print(a,b,c,d,e)

#tuple slice:x[start index:end index]
x=1,3,3.56,'hello','python'
y=x[1:4]
z=x[:3]
a=x[2:]
b=x[:]
print(y,z,a,b)

#tuple concatenation
a=1,2,3
b='a','b','c'
a+b
b+a
print(a+b)
print(b+a)

#adding elements to a tuple
a=1,2,3
a=a+(4,5)
print(a)
print(id(a))
b=1,2,3
b=(4,5)+b
print(b)
print(id(b))

#inserting elements in tuples
x=(1,2,3,4,5)
a=x[:3]
b=x[3:]
x=a+('Hello','python')+b
print(x)

#tuple:loops
my_tuple=(1,2.3,3,'hello')
for x in my_tuple:
    print(x)
    print('----')

#count method
x=(1,2,1,2,'hello',2.3,2)
x.count(2)
print(x.count(2))

#index retrieval
a=(1,2,3,2,'hello',2.3,2)
print(a.index(2))
print(a.index('hello'))

#variable swap
a=1
b=1
c=a,b=b,a
print(c)
