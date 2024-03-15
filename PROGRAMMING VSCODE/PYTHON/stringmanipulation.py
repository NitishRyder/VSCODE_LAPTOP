A='Hello'          #length of the object
print(len(A))

x='Tyler Durden'
print(len(x))

a='  \tmarla singer  '   #Removing whitespaces       
print(a.strip())

x='What are we? Consumers!'   #replace
print(x.replace('w','x'))

x='What%20is%20my%20%20address'
print(x.replace('%20',' '))

x='Hello,my,python'     #split
x.split(',')
print(x.split(','))

x='Hello world'    #deleting
del x


x='''Marla, hte big tourist.              
her lie reflected my lie,
and suddenly, I felt nothing.'''      #counting 
x.count('lie')
print(x.count('lie'))
x.count('dd')
print(x.count('dd'))

#slice:a[startIndex:endIndex]
b='Hello, Python'
b[2:6]
print(b[2:6])

#no.of word in the string
x='On a long enough timeline, the survival rate for everyone drops to'
'on' in x
'Timeline' in x
'timeline' in x
print('on' in x,'Timeline' in x,'timeline' in x)


b='Hello, Python'     #slicing,#extracting substrings
b[2:6]
print(b[2:6])

b='abcxyz'
b[:3]
print(b[:3])

b="hello, python"
b[3:]
print(b[3:])

b='hello'
b[-4:-1]
print(b[-4:-1])

a='hello'              #provides a copy
a[:]
print(a[:])



