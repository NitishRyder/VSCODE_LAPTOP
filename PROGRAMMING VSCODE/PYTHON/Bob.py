n= float(input("Enter amount in hand"))
c= float(input("Enter price of one chocolate"))
m= int(input("Enter num of wrappers for free chocolate"))
p=n//c
f=p//m
print("Number of chocolates", int(p+f))
