def f1():
    print("Hello, Python")
print("Outside function")
f1()
f1()

#functions are objects
def f1():
    print("Hello,Python")
f2=f1
f2()
f1()
f1=10
print(f1)

#Parameters and Arguments

def add(x,y):
    print(x+y)
add(1,2)
add(2,1)
add("hello","python")
add("python","hello")

#Return keyword
def calc_age(yob,curr_year):
    age = curr_year - yob
    return age

my_age = calc_age(2007,2021)
print(my_age)

#default return
def add(x,y):
    print(x+y)
z=add(1,2)
print(z)

def add(x,y):
    return x+y     #straight below the return st. is never executed
    print(x+y)
z= add(1,2)
print(z)

#conditional return
def larger(x,y):
    if x>=y:
        return x
    else:
        return y
z=larger(6,3)
print(z)
a=larger(5,10)
print(a)


def f1():
    return 1,2
z=f1()
print(z)

#Quiz

def f1(a,b):
    c = a+b
print(f1(2,3))
print(f1('my','dear'))

def f1(a,b):
    return a+b


#Keyword Arguments
def calc(x,y,z):
    return(x-y)/z

z1=calc(y=4,z=3,x=10)          #all keyword args
z2=calc(10,4,3)                #all positional args
print(z1)
print(z2)

def calc(a,b,c):
    print((a+b)/c)
calc(a=1,b=2,c=3)
calc(b=2,a=1,c=3)
calc(c=3,a=1,b=2)
calc(c=3,b=2,a=1)

#mixing and adding(positional args and keyword args)
def f1(a,b,c):
    print(a,b,c)
f1(1,2,3)
f1(1,2,c=3)             #f1(a,b=2,c=3),f1(a=1,2,3),f1(1,b=2,3)causes error
f1(b=2,a=1,c=3)         #positional args must come before all keyword args
f1(1,c=3,b=2)


#default values for parameters
def f1(a=10,b=20,c=30):
    print(a,b,c)
f1(1,2,3)
f1()
f1(1)
f1(1,2)

#Mix default and non-default parameters

def f1(a,b=99,c=999):
    print(a,b,c)
f1(1,2,3)
f1(1)
f1(1,2)

def f1(a=9,b=99,c=999):
    print(a,b,c)
f1()
f1(1)
f1(1,2)

def f1(a=9,b=99,c=999):
    print(a,b,c)
f1.__defaults__
print(type(f1.__defaults__))


#variable arguments

def get_ages(*birth_year):
    for x in birth_year:
        print(2021-x)
get_ages(2003,2007)
get_ages(1913,1945,1971,2000)
get_ages(2001,2010,1989)

#variable keyword args

def my_func(**kwargs):
    print(kwargs)

my_func(a=1,b=2,c=3)
my_func(lat=13.1,lont=12.35)


def f1(x=[]):
    x.append('a')
    print(x)
f1()
f1()
f1()

#Function variable scope

def f1(y):
    x=10
    return x+y
a=20
b=f1(a)
print(b)

#global Access to local:No!
def f1():
    x=10
    y=20
    return x+y
z1 = f1()
print(z)

#Local access to Global Variable:Yes!
x=1
def f1():
    print(x)
f1()
print(x)

x=2000                      #id's also samee
def f1():
    x=2000
    print(x,id(x))
f1()
print(x,id(x))

#Local changes Global variable
x=1
def f1():
    global x
    x=100
    print(x,id(x))
f1()
print(x,id(x))

x=1
def f1(x):
    print(x,id(x))
    x=100
    print(x,id(x))
f1(x)
print(x,id(x))


x=1
def f2():
    print(x)
f2()
print(x)
f2.__code__.co_varnames

#Global Mutable Objects

x=[]
def f1(a):
    print(a)
    a.append(100)
    print(a)
f1(x)
print(x)

#Lambda Functions

def add(x,y):
    return x+y
# By using lambda this can be coded as
lambda x,y : x+y
add = lambda x,y : x+y
print(add(1,2))
print(add(3,3))


x = ['a','titan','mars','eros','ganemyde','io']
x.sort(key = lambda y:len(y))
print(x)

x.sort(key=lambda y:y[-1])
print(x)

x = 1
def f1(x):
    print(x)
f1(999)
print(x)

