num=int(input())
new_list=[]
for j in range(num):
  d=input()
  new_list.append(d)
second_list=new_list.copy()
few=[]
for k in range(len(second_list)):
  x=second_list[k]
  if x[0]=='y':
   new_list.remove(x)
   few.append(x)
n=sorted(new_list)
m=sorted(few)
print(m+n)