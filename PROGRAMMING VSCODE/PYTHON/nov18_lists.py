#LISTS

l1=[1,2,3,4,5,6]
print(l1[3])

l1=[1,2,3,4,5,6]
l1[2]=111
print(l1)

l1=[1,2,3,4,5,6]
del(l1[4])
print(l1)

print(len([1,2,3]))

a=str([1,2])+'34'
print(a)
b=[1,2]+list('34')
print(b)
 
a=list(map(abs,[-1,-2,0,1,2]))
print(a)

b=list(map(abs,[-1,-2,-4,-10]))
print(b)



