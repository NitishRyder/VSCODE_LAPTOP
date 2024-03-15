a='HelloWorld'     #assig 1
b=a[:1]+a[-1:]
print(b)

x=input('Enter the name:')       #assig 2
y=input('Enter the age:')
print(f'Hello {x}!')
print(f'You are {y} years old')

#assig 3
print("Father: 'How are you?'\nSon: 'I am fine. However, my friend is not doing too well'")
 
#assig 4
a='nitish'
b='n'.upper() + a[1:]
print(b)

#assig 5
x='python'
b='t'*100
c=x+b
print(c) 

#assig 6
x='hello'
y=x+x[2]*100
print(y)

#isalnum
x='abc123'            #true only for alphanumeric characters
y='abc 123'
z='3.14'
print(x.isalnum())
print(y.isalnum())
print(z.isalnum())

#assig 7
x='call me ishmael'
y=x.title()
z=x.capitalize()
print(y)
print(z)

#assig 8
x='seventy'
x[1:6]
print(x[1:6])
y='hello python!'
y[4:9]
print(y[4:9])

x='seventy'
middle=((len(x)-1)/2)
print(int(middle))
middle=int(middle)
y=x[middle- 2: middle + 3]
print(y)

#assig 9
x=[1,2,3,4]
index = -1
newx=[None] * len(x)
for e in x:
    newx[index]=e
    index-=1
x=newx
print(x)


#assig 10
weights=[180,190,190,191,200,190]
progress_days=0
for index in range(2,len(weights)):
    if (weights[index]> weights[index-1]) and (weights[index]>weights[index-2]):
        progress_days+=1
print(progress_days)


#assig 11
table = ['A-S','10-S','2-D','3-H','7-S']
hand = ['3-S','5-S']
table_suits = ''
hand_suits = ''
for e in table:
    suit = e.split('-')[1]
    hand_suits += suit
for e in hand:
    suit = e.split('-')[1]
    hand_suits += suit

all_suits = table_suits + hand_suits

count = {}
count['H'] = all_suits.count('H')
count['S'] = all_suits.count('S')
count['D'] = all_suits.count('D')
count['C'] = all_suits.count('C')

for s,c in count.items():
    if c >=5:
        print(f'you have a flush of {c} cards in {s}')
        break
    else:
        print('You have no flushes')


#assig 12

s1= 'belowxbx'
s2= 'elbowxxb'
hamming = 0

for e in s1:
    if s1.count(e) != s2.count(e):
        print('They are not anagrams')
        break
    else:
        print('yes, they are anagrams')
        index=0
        for e in s1:
            if e != s2[index]:
                hamming += 1

            index += 1
        print('The Hamming distance is:',hamming)  


#assig 13
x=input('Enter numbers separated by commas:')
my_list = x.split(',')
index = 0

for e in my_list:
    my_list[index] = int(e)
    index += 1
print(my_list)

#assig 14
start =1000
stop = 4000
for en in range(start,stop+1):
    str_en = str(en)
    for ec in str_en:
        if int(ec)%2 != 0:
            break
    else:
        print(en)


#assig 15
word = 'hellopython'
final = ['_']*len(word)
index = 0
guess = input('Please enter a character:')

for e in word:
    if guess == e:
        final[index] = e
    index += 1

print(final)
                    

#assig 16
tax_brackets = [
    (0,10000,0),
    (10000,20000,0.05),
    (20000,50000,.1),
    (50000,100000,.15),
    (100000,float('inf'), 0.2)
]

income = 16000
tax = 0
for each in tax_brackets:
    if income > each[1]:
        tax = tax + (each[1] - each[0]) * each[2]
    else:
        tax = tax + (income - each[0])*each[2]
        break
print(tax)

#assig 17
x=[(3,'Santino'),(1,'Vito'),(4,'Fredo'),(10,'Tessio'),(7,'Connie'),
(9,'Clemenza'),(2,'Michael')]
print(x)

def sort_order(each_element):
    return each_element[0]
x.sort(key=sort_order)
print(x)

#assig 18
def f1(x=[]):
    x.append(len(x))
    return x
print(f1([2,6,7]))

print(f1(['hello',22.3,1,'python']))
print(f1())
print(f1())
print(f1())
print(f1())

def f1(x=[]):
    x.append(len(x))
    return x
print(f1())
print(f1())
print(f1())                 #f1.__defaults__ stores all default values


def f1(x=[]):
    x.append(len(x))
    return x
print(f1.__defaults__)

print(f1([1,2,3]))
print(f1.__defaults__)

print(f1(['a',2.3,3,7,100]))
print(f1.__defaults__)

print(f1())
print(f1.__defaults__)

print(f1())
print(f1.__defaults__)

print(f1())
print(f1.__defaults__)

def f1(x=None):
    if x==None:x=[]
    x.append(len(x))
    return x

#assig 19
def ages(father,mother,child):
    age_father = child - father
    age_mother = child - mother
    if age_father<18 or age_mother<18:
        print('One or more parent age is too low')
    elif age_father > 60 or age_mother >60:
        print('One or more parent age is too high')
    else:
        print('Fathers age:',age_father)
        print("Mothers age:",age_mother)
ages(1951,1975,2012)


#assig 20
def calc(x,y):
    return x+y,x-y,x*y,x/y
print(calc(2,1))
print(calc(5,3))


#assig 21

def swap(my_dict):
    swapped_dict={}
    for k,v in my_dict.items():
        swapped_dict[v]=k
    return swapped_dict
x={1:'one',2:'two',3:'three'}
print(swap(x))


#assig 22
def max_l(my_list):
    my_max = float('-inf')
    for e in my_list:
        if e > my_max:
            my_max = e
    return my_max
print(max_l([-1,-2,3,0]))


#assig 23
def count_case(s):
    lower_case = 0
    upper_case = 0
    for e in s:
        if e.isupper():upper_case+=1
        elif e.islower():lower_case+=1
    return upper_case,lower_case
print(count_case('Hello,Python!'))
print(count_case('HELlo'))
print(count_case('python'))
