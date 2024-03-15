x=[1,3,3.56,'hello']
count=0
for e in x:
    print(count,e)
    count+=1

#Enumerate function
print("ENUMERATE FUNCTION")
x = [1,3,3.56,'hello']
for count,e in enumerate(x):
    print(count,e)

x = [1,3,3.56,'hello']
for count,e in enumerate(x,3):
    print(count,e)


x={'io','europa','eros','ganymede'}
print(list(enumerate(x)))


#for dictionary only keys we get in output
x={'fname':'james',
    'IName':'Holden',
    'occupation':'captain',
    'ship':'Rocinante'}
y=enumerate(x)
print(list(y))
for e in enumerate(x):
        print(e)


#map function              #using lambda
print("MAP FUNCTION")
x = [1,3.56,7,-3,25.4]
def squares(n):
    return n**2
y=map(squares,x)
y=list(y)
print(y)

y=map(lambda n:n**2,x)
y=list(map(lambda n:n**2,x))
print(y)

x = [1,3.56,7,-3,25.4]
print(map(lambda n:n**2,x))


x=['io','europa','eros','ganemyde']
y=[1,2,3,4]
def combine(e1,e2):
    return e1+'_'+str(e2)
z=map(combine,x,y)
print(list(z))

z=list(map(lambda e1,e2:e1+'_'+str(e2),x,y))
print(z)


#using map func. in 3 lists
id = [10234,56231,94523,71234,68123]
fName = ['James','Naomi','Amos','Alex']
lName = ['Holden','Nagata','Burton','Kamal']
def combine(e1,e2,e3):
    return e1,e2+''+e3
y=map(combine,id,fName,lName)
print(dict(y))

y=dict(map(lambda e1,e2,e3:(e1,e2+''+e3),id,fName,lName))
print(y)

#FILTER FUNCTION
#apply some logic to each element,(keep if True,Drop if False)

x=[1,3,7,8,9,5]
def greater5(n):
    return True if n>5 else False
y=filter(greater5,x)
print(x)
print(list(y))

#REDUCE FUNCTION
#reduces an iterable to single value based on some logic

x=[1,2,3,4,5]        #instead of using for loop we use reduce func

from functools import reduce
def add(e1,e2):
    return e1+e2
sum =reduce(add,x)
print(sum)

sum=reduce(lambda e1,e2:e1+e2,x)
print(sum)

#using REDUCE FUNC to find the min value in a list
min=reduce(lambda e1,e2:e1 if e1<e2 else e2,x)

x=[3,5,7,1,9]
min=reduce(lambda e1,e2:e1 if e1<e2 else e2,x)
print(min)

#zip function
#combine iterables element by element

x=[1,2,3]
y=('a','b','c')
z=['!','@','#']
print(zip(x,y,z))
print(list(zip(x,y,z)))

h=[1.2,3.4,4.4]
print(list(zip(x,h)))

#zip function in for loop
for e1,e2 in zip(x,y):
    print(e1,e2)

print(dict(zip(x,y)))

#CLOSURes

x='Global X'
def f2():
    print(x)

def f1():
    x='f1 X'
    print(x)
    f2()
f1()

#Nested functions

x='Global X'
def f1():
    x='f1 X'
    def f2():
        print(x)
    f2()
f1()

#LEGB Rule
def f1():
    #x='f1 x'
    def f2():
        id='f2 id'
        print(id)
    f2()
f1()


#define a function inside another function and execute it outside.

def f1():
    def f2(n):
        print('Inner function f2',n)
    return f2
y=f1()
y(5)
y('is executing')
del f1   #it has no effect in output
y(10)

#Inner function uses local variable of Outer function
x='GLobal x'
def f1():
    x='f1 x'
    def f2():
        print(x)
    return f2
y=f1()
y()
y.__closure__[0].cell_contents
y.__code__.co_freevars


#closures

food = "Junk food"
def mother():
    food="Healthy food"
    def child():
        print("Eating",food)
    return child
child1=mother()
child1()

def add4(n):
    print(n+4)
def add5(n):
    print(n+5)
def add6(n):
    print(n+6)

def outer(x):
    def adder(y):
        print(y+x)
    return adder

add4=outer(4)
add5=outer(5)
add6=outer(6)
add4(10)
add5(20)
add6(30)

print(add4.__closure__)
print(add4.__closure__[0].cell_contents)
print(add4.__code__.co_freevars)


#Decorators
#Powerful Python Tool,Little complex in the beginning,Uses closures
#Decorators enhance a function,Dont change the core function,Stack multiple decorators

def d1(anyfunc):
    def wrapped():
        print(anyfunc, 'started')
        y=anyfunc()
        return y
    return wrapped

def base():
    print("I am base function")
new_base=d1(base)    
type(new_base)
new_base()

print(new_base.__closure__)
print(new_base.__closure__[0].cell_contents)
print(new_base.__code__.co_freevars)

import dis
dis.dis(new_base)
print(dis.code_info(new_base))

def f1():
    y=100
    print('THe value of y is:',y)
new_f1=d1(f1)
new_f1()

base=d1(base)
base()
f1=d1(f1)
f1()

#base=d1(base) or @d1

@d1
def base():
    print("I am base function")
@d1
def f1():
    y=100
    print("The value of y is:",y)

#Decorate functions with parameters

def d1(anyfunc):
    def wrapped(*args,**kwargs):
        print(anyfunc,'started')
        y=anyfunc(*args,**kwargs)
        return y
    return wrapped

@d1
def add(a,b):
    return a+b
z=add(2,3)
print(z)

#Multiple Decorators

def d2(anyfunc):
    def wrapped(*args,**kwargs):
        x=anyfunc(*args,**kwargs)
        print(anyfunc,'ended')
        return x
    return wrapped

@d2
@d1
def base():
    print("I am base function")
base()

#Decorator Example
import time
def fn_time(anyfunc):
    def wrapped(*args,**kwargs):
        start_time=time.time()
        y=anyfunc(*args,**kwargs)
        execution_time=time.time()-start_time
        print(f'Function{anyfunc}took{execution_time}seconds')
        return y
    return wrapped

@fn_time
def power2(n):
    return 2**n
result=power2(1000)
print(result)

#List Comprehensions

