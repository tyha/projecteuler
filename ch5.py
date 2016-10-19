#Smallest multiple

def valid(n):
    for i in reversed(range(2,21)):
        if(n%i != 0):
            return False
    return True

n=2*3*5*7*11*13*17*19
while(not valid(n)):
    n+=2*3*5*7*11*13*17*19

print(n)
