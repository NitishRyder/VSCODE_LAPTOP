lst=[1,2,4,8,9]
odd_sum=sum(n for n in lst if n % 2 != 0) 
print(odd_sum)
even_sum=sum(n for n in lst if n %2==0)
print(even_sum)
pos_div=odd_sum/even_sum
print(pos_div)

lst1=[10,20,13,17,30]
odd_sum1=sum(n for n in lst1 if n % 2 != 0) 
print(odd_sum1)
even_sum1=sum(n for n in lst1 if n %2==0)
print(even_sum1)
pos_div=odd_sum1/even_sum1
print(pos_div)

lst2=[10,20,30,40,50]
odd_sum2=sum([n for n in lst2 if n % 2 != 0]) 
print(odd_sum2)
even_sum2=sum(n for n in lst2 if n %2==0)
print(even_sum2)
def pos_div(z):
    for k in range(0,len(z)):
        if odd%2==0:
            even_sum2.append(z[k])

