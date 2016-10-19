#10001st prime
import math

def prime(n):
    if(n==2):
        return True
    if(n<=1 or n%2 == 0):
       return False
    for i in range(3, int(math.sqrt(n))+1,2):
        if(n%i==0):
            return False
    return True

def nextPrime(n):
    p=n+1
    while(not prime(p)):
        p+=1
    return p
    
p=1
for i in range(10001):
    p = nextPrime(p)
print(p)
