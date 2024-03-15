L=['eat','more','spam']
L.append('please')
print(L)

#sorting
L=['eat', 'more', 'SPAM!', 'please']
L.sort()
print(L)

#sorting with mixed case
L=['abc','ABD','aBe']
L.sort()
print(L)

#normalize to lowercase
L=['abc','ABD','aBe']
L.sort(key=str.lower)
print(L)

#change sort order
L=['abc','ABD','aBe']
L.sort(key=str.lower,reverse=True)
print(L)

#Extend
L=[1,2]
L.extend([3,4,5])
print(L)

#removing items
L=[1,2,3,4,5]
L.pop()
print(L)

#Reverse
L=[1,2,3,4]
L.reverse()
print(L)

L=['abc','ABD','aBe']
print(L.index('ABD'))

L=['spam','more','spam','eat','spam']
print(L.count('spam'))


#conversion
S='spammy'
L=list(S)
print(L)
L[3]='x'
L[4]='x'
print(L)

#uses '' for joining elements of lists
S=''.join(L)
print(S)

#uses 'SPAM' for joining elements of list
A='SPAM'.join(['eggs','sausage','ham','toast'])
print(A)



