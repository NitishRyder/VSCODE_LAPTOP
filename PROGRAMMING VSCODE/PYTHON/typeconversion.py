#numeric conversion

# int to float:float()
print(float(1))
print(float(-1))
#float to int:int()
print(int(1.2))
print(int(1.7))
print(int(-1.7))

#STRING conversion
#string to float:float()
print(float('1.2'))

#string to int:int()
print(int('7'))

#string to tuple:tuple()
print(tuple('hello'))

#string to list:list()
print(list('hello'))

#string to set:set()
print(set('hello'))


#TUPLE conversion

#tuple to list:list()
x=(1,2,3)
print(list(x))

#tuple to set:set()
x=(1,2,3,2)
print(set(x))

#tuple to dictionary:dict()
x=((1,'a'),('b',23))
print(dict(x))


#LIST conversion

#list to tuple:tuple()
x=[1,2,3]
print(tuple(x))

#list to set:set()
x=[1,2,3,2]
print(set(x))


#SET conversion

#set to tuple:tuple()
x={1,2,3}
print(tuple(x))

#set to list:list()
x={1,2,3,4}
print(list(x))


#QUIZ

x=['a','b','a','x']
x=list(set(x))
print(x)