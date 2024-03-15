import math
#step1: selecting 2 publicly known numbers
q=int(input("Enter a prime number:"))
alpha=int(input("Enter a primitive root of prime number:"))
#step2: selecting random integer as private key
xa=int(input("Enter first random integer:"))
xb=int(input("Enter second random integer:"))
#step3: calculating public key
ya=pow(alpha,xa)%q
yb=pow(alpha,xb)%q
print("Sender Private key=",xa)
print("Sender Public key=",ya)
print("Receiver Private key=",xb)
print("Receiver Public key=",yb)
#step4: compute key
xak=pow(yb,xa)%q
yak=pow(ya,xb)%q
print("Sender secret key(Alice)=",xak)
print("Receiver secret key(Bob)=",yak)
#step5: check whether they are same
if(xak==yak):
 print("Both secret keys are same")
else:
 print("Secret keys are different")
