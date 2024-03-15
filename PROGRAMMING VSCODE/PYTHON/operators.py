#ARITHMETIC,#ASSIGNMENT,#COMPARISON,#LOGICAL,#IDENTITY,#MEMBERSHIP,#BITWISE
 

#arithmetic and assignment
X=5
X+=3
print(X)
x=5
x-=3
print(x)
x=5
x*=5
print(x)
x=5
x/=3
print(x)
x=5
x//=3
print(x)
x=5
x%=3
print(x)
x=5
x**=3
print(x)

#COMPARISON
print(bool(10==10))
print(bool(20==45))
print(bool('hello'=='hello'))

print(bool(10!=10))
print(bool(10!='hello'))
print(bool('xyz'!='xyz'))

print(bool(7>3))
print(bool(6>10))

print(bool(1>=1))
print(bool(7<=1))

#LOGICAL --- AND,OR,NOT

print(bool(7>3 and 8<10))
print(bool(7>3 and 8<6))
print(bool(10<=15 and 'hello'=='hello'))

print(bool(7>3 or 8>4))
print(bool(7>3 or 8<4))
print(bool(7>10 or 8<4))

print(bool(not 7>10))
print(bool(not 8>2))

#compound operator
print(bool(7>3 and not 6>3 or 5>3))        #not is evaluated first
                                           #secondly and is evaluate

print(bool(7>3 and not (6>3 or 5>3)))      #with parenthesis


#IDENTITY 

a=1000
b=a
print(bool(a==b))
print(bool(a is b))
print(id(a))
print(id(b))

#membership operators

print(bool('h' in 'hello'))
print(bool('H' in 'hello'))
print(bool('p' not in 'simple'))
print(bool('x' not in 'ryder'))

#BITWISE

print(0b1)
print(0b11)

#Bitwise AND
print(bin(0b1101 & 0b1001))          

#Bitwise OR
print(0b1010 | 0b0011)
print(bin(0b1010|0b0011))

#right shift
print(bin(0b1100>>2))

#left shift
print(bin(0b1100<<3))

#QUIZ
x=[1,2,3]
a=1
b=4
print(a in x)
print(b in x)

print(bool(8>=7))
print(bool(7<=7))