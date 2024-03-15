word='python lobby'
vowel=0
consonant=0
space=0
for i in word:
    if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or
    i=='E' or i=='I' or i=='O' or i=='U'):
        vowel=vowel+1
    elif(i==' '):
        space=space+1
    else:
        consonant=consonant+1
print("Count of Vowel is:",vowel)
print("\nCount of Consonant is :%d" %consonant)
print("\nCount of White space :%d"%space)

#NAVA PAT3
def sum_of_primes(num):
    isPrime = 1
    for i in range (2,int(num/2),1):
        if(num % i == 0):
            isPrime = 0
            break
    return isPrime

num = 40
flag = 0;
i = 2
for i in range (2,int(num/2),1):
    if(sum_of_primes(i) == 1):
        if(sum_of_primes(num-i) == 1):
            print(i,num-i)
            flag = 1;
if (flag == 0):
    print(num,"cannot be expressed as the sum of two prime numbers")
