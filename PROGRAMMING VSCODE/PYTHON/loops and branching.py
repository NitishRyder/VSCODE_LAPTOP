#FOR LOOP(using range function)

for x in range(5):
    print(x)
for x in range(3,8):
    print(x)
for x in range(3,10,3):
    print(x)


# IF:BRanching (if-elif-else)

age=66
if age>65:
    print("Pension eligible")
else:
    print("Pension ineligible")
    print("some other code")

age=64
if age>65:
    print("Pension eligible")
else:
    print("Pension ineleigible")
    print("some other code")


age=65
if age>65:
    print("Pension 100%")
elif age<=65 and age>=60:
    print("50% pension eligible")
else:
    print("Pension 0%")
print("Some other code")


#Ternary Expressions(short way to write if,ifelse)
x=10
y=5
if x>y:print("x is greater than y")

x=10
y=5
print("x") if x>y else print("y")

a=10
b=20
max= a if a>b else b
print(max)

a=110
b=20
max= a if a>b else b
print(max)


age=65
pension='100%' if age>65 else '50%' if age<=65 and age>=60 else '0%'
print(pension)


#WHILE LOOP

x=0
while x<5:
    print(x)
    x+=1

#break and continue

for x in range(5):
    if x==2:continue
    print(x)

for x in range(5):
    if x==2:break
    print(x)

for x in range(10):
    if x==2:continue
    if x==7:break
    print(x)

x=0
while x<5:
    print(x)
    x+=1
print('some other code')

#QUIz

x=[1,2,3,4]
total=0
for e in x:
    total+=e
print(e,total)

x=['hello','python']
y=set()
for e in x:
    for e2 in e:
        y.add(e2)
print(y)


x=-1
while x<10:
    x+=1
    if x%3==0:
        continue
    print(x,end='')


x='abc'
for e in x:
    print(e+x)


x=4
for i in range(5):
    z=x+i if x>i else x-i
    x-=1
    print(z)