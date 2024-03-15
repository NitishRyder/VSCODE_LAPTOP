# dictionaries are unordered,mutable(add,delete,update value after creation) and indexed key-value pairs
#(keys must be hashable,values can be any python object)
#duplicate keys are not allowed


#DICTIONARY ACCESS
x=dict(name='John',age=35,city='NYC')
print(x)
print(type(x))

x={'name':'John','age':'35','city':'NYC'}   #Access to value is only through the key
print(x['name'])
print(x.get('city'))

x={'name':'John','age':'35','city':'NYC'} 
for k in x:
    print(k)              #only keys 
for k in x:
    print(x[k])           #only values
for val in x.values():
    print(val)            #only values
for k,v in x.items():
    print(k,v)            #key,values


my_dict = {'germany':'berlin','india':'newdelhi','USA':'washington'} 
print(my_dict['germany'])


my_dict={'germany':['berlin',300000,'Angela Merkel'],'india':['newdelhi',10000000,'narendra_modi']}
print(my_dict['india'][1])
my_dict['india'][2]='rahul_gandhi'
print(my_dict['india'][2])


#Dictionary Add and change
x={'name':'John','age':35,'city':'NYC'} 

x['age']=40            #update an existing key:value pair
print(x)

print(x.update({'zip':10029,     #add or update multiple key:value pairs(s)
'state':'NY',
'age':40}))

x['zip']=10029                    #add a new key:value pair
print(x)

#dictionary check key and length
x={'name':'John','age':35,'city':'NYC'} 
print('name' in x)
print('zip' in x)
print(len(x))

#dictionary key:value removals
x={'name':'John','age':35,'city':'NYC'} 
x.pop('age')
print(x)
del x['city']
print(x)
x.clear()                   #removes all,Leaves empty dict.
print(x)                    # del x (entire dict. is erased)


#dictionary copy
x={'name':'John','age':35,'city':'NYC'} 
y=x.copy()                   #y=x will not work to create a copy
print(y)                     # id(x) and id(y) are different
y=dict(x)
print(y)
print(id(x))
print(id(y))


#quiz
x={1:1,2:2,3:3}
y={1:4,2:5}
x.update(y)
print(x)