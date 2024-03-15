#Set is a collection and unordered,immutable,indexing is not possible
#No duplicates is allowed,Sets are iterable
s2={5,6,4,2,1,2}
print(s2)

x={1,2,3,4}
y={'apple','ball','cat'}
x1=set('spam')                   #prepare set from a string
print(x1)

x1.add('alot')                   #add an element to the set
print(x1)

#set operations

s1={1,2,3,4}             #union(|)
s2={1,5,3,6}|s1
print(s2)

s2=s1&{1,3}              #intersection(&)
print(s2)

s2=s1-{1,3,4}            #difference(-)
print(s2)

s2=s1>{1,3}              #super set(>)
print(s2)

s2=s1-{1,2,3,4}
print(s2)                #empty set


cities={'Stuttgart','Konstanz','Freiburg'}
cities.clear()
print(cities)

more_cities = {'Winterthur','Schaffhausen','St.Gallen'}
cities_backup = more_cities.copy()
more_cities.clear()
print(cities_backup)                        #copied value is still available

#difference_update()
x={'a','b','c','d','e'}
y={'b','c'}
x.difference_update(y)
print(x)

#discard(ele)
x={'a','b','c','d','e'}
x.discard('a')
print(x)

x.discard('z')
print(x)

#remove(ele)
x={'a','b','c','d','e'}
x.remove('a')
print(x)

#isdisjoint()
s1={1,2}
s2={3,4}
s3={1,2,3,4}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

#issubset()
print(s1.issubset(s3))




