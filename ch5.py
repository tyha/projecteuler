#Smallest multiple

def valid(n):
    for i in reversed(range(2,21)):
        if(n%i != 0):
            return False
    return True

#multiple of prime numbers under 20
a=2*3*5*7*11*13*17*19

n=a
while(not valid(n)):
    n+=a

print(n)
