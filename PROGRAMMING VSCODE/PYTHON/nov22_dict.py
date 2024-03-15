#Dictionary(pair of items,each pair has key and value,keys should be unique)
#(key and value are separated by:,Each pair is separated by,)

MyDict = {1:'Chocolate',2:'Icecream'}
print (MyDict[1])
MyCourse = {'MS':'Python', 'IT' : 'C' ,'CSE':'C++','MCA':'Java'}
print(MyCourse['CSE'])


#Updating ELements
MyDict = {1:'Chocolate',2:'Icecream'}
MyCourse = {'MS':'Python', 'IT' : 'C' ,'CSE':'C++','MCA':'Java'}
MyDict[1]='Pizza'
MyCourse['MCA']='UML'
print(MyDict)
print(MyCourse)

#Deleting elements

MyCourse = {'MS':'Python', 'IT' : 'C' ,'CSE':'C++','MCA':'Java'}
del MyCourse['IT']
print(MyCourse)

MyCourse.clear()                  #clear gives a empty dict in output
print(MyCourse)

#Basic operations
D={'spam': 2, 'ham': 1, 'eggs': 3}
print(len(D))
print('ham' in D)
print(list(D.keys()))
print(D.values())
print(list(D.items()))
print(D.get('spam'))
print(D.get('toast'))


#Update Method
D={'eggs':3,'spam':2,'ham':1}
D2={'toast':4,'muffin':5}
D.update(D2)
print(D)             #unordered

#pop method
D={'eggs': 3, 'spam': 2, 'ham': 1, 'toast': 4, 'muffin': 5}
D.pop('muffin')
D.pop('toast')
print(D)


#Nesting in Dictionaries
jobs = []
jobs.append('developer')
jobs.append('manager')
rec={}
rec['name']



