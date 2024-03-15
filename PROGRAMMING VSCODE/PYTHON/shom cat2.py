def Reverse(lst):
	lst.reverse()
	return lst
lst = [10,20,30,40]
a=(Reverse(lst))

def Reverse(lst1):
	lst1.reverse()
	return lst1
lst1 = [4,5,6,7,8]
b=(Reverse(lst1))

i = [10,20,30,40]
j= [40,30,20,10]
odd_sum =int(i[0]+i[2])
even_sum =int(i[1]+i[3])

k=[i[0]+j[0],i[1]+j[1],i[2]+j[2],i[3]+j[3]]
print(k)

pos_mul=odd_sum*even_sum
print(pos_mul)