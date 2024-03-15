#insertion sort

def insertion_sort(items):
    for i in range(l,len(items)):
        j=i
        while j>0 and items[j]>items[j-1]:
            items[j],items[j-1]=items[j-1],items[j]
            j-=1
        items[j]

#bubble sort

def bubblesort(lyst):
    n=len(lyst)
    while n>1:
        i=1
        while i<n:
            if lyst[i]<lyst[i-1]:
              (lyst,i,i-1)
            i+=1
        n-=1

def bubble(l):
    n=len(l)
    for i in range(0,n-l):
        for j in range(0,n-l):
            if l[j][2]<l[j+1][2]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
n=int(input())
l=[]
for i in range(0,n):
    name=input()
    addr=input()
    score=float(input())
    l.append((name,addr,score))
l=bubble(l)
print(l)