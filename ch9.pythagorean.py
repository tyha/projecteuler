# Special Pythagorean triplet
import math

for a in reversed(range(1,333)):
    for b in range(a+1,999):
        if(a>=b):
            break
        c = math.sqrt(a**2+b**2)
        if(a+b+c > 1000):
            break
        if(a+b+c==1000.0):
            print (a,b,c)
