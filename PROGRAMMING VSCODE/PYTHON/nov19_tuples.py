#Tuples re immutable,cannot be changed like lists,Tuples use parentheses

tup1 = ('physics','chemistry',1997,2000)
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d"

print(tup1[0])
print(tup2[1:5])
print(tup3[:3])


#concatenation,Repetition,indexing and slicing

A = (1,2)+(3,4)
print(A)
B = (1,2)*4
print(B)
C= (1,2,3,4)
print(C[0],C[1:3])

#sorted method in tuples
tmp = ['aa', 'bb', 'cc', 'dd'] 
T=tuple(tmp)
print(T)

T=(1,2,3,4,5)
L=[x+20 for x in T]
print(L)

#Index method
T=(1,2,3,2,4,2)
print(T.index(2))
print(T.index(2,2))
print(T.count(2))

#Nested Tuples
T=(1,[2,3],4,[5,6])
T[1][1]='hello'
T[3][1]='world'
print(T)

#Tuple record
bob=('Bob',40.5,['dev','mgr'])
print(bob[0],bob[2])

#prepares a dictionary record from tuple
bob = dict(name='Bob',age=40.5,jobs=['dev','mgr'])
print(bob)
print(bob['name'],bob['jobs'])

#Basic Tuples operations

print(len((1,2,3)))                #length
print((1,2,3)+(4,5,6))             #concatenation
print(('Hi!')*4)                   #Repetition
print(3 in (1,2,3))                #Membership
for x in (1,2,3):                  #Iteration
    print(x)

#Indexing and Slicing

l=('spam','Spam','SPAM!')
print(l[2])
print(l[-2])
print(l[1:])

#Built in Tuple Functions
tuple1,tuple2 = (123,'xyz'),(456,'abc')
print(len(tuple1))

t1=(1,2,3,7,4)
print(max(t1))
print(min(t1))


Lab_reading={'test1':(20,30),'test2':(35.5,40),'test3':(12,15),'test4':(120,150),'test5':(80,120)}
Lab_reading={}
for i in range(0,5):
    test_Name = input()
    min = float(input())
    max = float(input())
    Lab_reading[test_Name] = (min,max)
print(Lab_reading)
#read name of test
chk_Test = input()
#read observed value of test
obs_value = float(input())
#find range of values for the specified test
range_test = Lab_reading[chk_Test]
min = range_test[0]
max = range_test[1]
if min<obs_value<max:
    print('Normal')
else:
    print('Abnormal')
