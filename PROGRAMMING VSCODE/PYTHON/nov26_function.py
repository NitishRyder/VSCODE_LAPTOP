#Assignment statements

[a,b,c] = (1,2,3)
print(a,c)
print(a,b,c)

(a,b,c)="ABC"
print(a,c)

seq=[1,2,3,4]
a,b,c,d = seq
print(a,b,c,d)

a,*b,c = seq
print(a)
print(b)
print(c)

a,*b='spam'
print(a,b)

a,*b,c = 'spam'
print(a,b,c)

a,*b,c=range(4)
print(a,b,c)

#Example Functions
def printer(message):
    print('Hello'+message)
def my_function(fname):            #actual arg
    print(fname+'Refsnes')
my_function('Emil')                #formal arg
my_function('Tobias')              
my_function('Linus')

def times(x,y):
    return x*y
times(2,4)
x=times(3.14,4)
print(x)

s1="SPAM"
s2="SCAM"


s1='SPAM'
s2='SCAM'
[x for x in s1 if x in s2]


a=4
if a%2==0:
    def func():
        print('even')
else:
    def func():
        print('odd')
func()

#function call through variable
def one():
    print('one')
def two():
    print('two')
def three():
    print('three')

a=2
if a==1:
    call_func=one
elif a==2:
    call_func=two
else:
    call_func=three
call_func()

#SCOPE of variables

x=88
def func():
    x=99
func()
print(x)

#accessing global variables
x=88
def func():
    global x
    x=99
func()
print(x)

y,z=1,2                          #global variables in module
def all_global():
    global x                     #declare globals assigned
    x=y+z                           
print (x)

#nested functions
x=99
def f1():
    x=88
    def f2():
        print(x)
    f2()
f1()

#return functions
def f1():
    x=88
    def f2():
        print(x)
    return f2
action =f1()
action()


def avg(n1,n2,n3):
    return(n1+n2+n3)/3.0
result=avg(10,25,16)*3
print(result)

#returning multiple variables
def multiple(x,y):
    x=2
    y=[3,4]
    return x,y

x=1
l=[1,2]
x,l=multiple(x,l)
print(x,l)

#Examples:
x=int(input())
y=int(input())
pt1=(x,y)
x=int(input())
y=int(input())
pt2=(x,y)
x=int(input())
y=int(input())
No=False
pt3=(x,y)
if fall_St_line(pt1,pt2,pt3):
    print('No Triangle')
    
    No=True
else:
    dist=calc_Distance(pt1,pt2,pt3)
    if dist_Check(dist):
        print('No Triangle')
        No=True
    if not No:
        print('Triangle')