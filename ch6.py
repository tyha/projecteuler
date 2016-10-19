#Sum square difference
s1,s2 = 0,0
for i in range(1,101):
    s1 += i
    s2 += i*i
 
print(s1*s1-s2)
