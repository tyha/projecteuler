#Largest prime factor
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
  i = n + 1
  while(not prime(i)):
    i += 1
  return i

a=600851475143
b=2
result = []
while(a != 1):
  while(a%b == 0):
    result.append(b)
    a = a / b
  b = nextPrime(b)
  
print(max(result))
