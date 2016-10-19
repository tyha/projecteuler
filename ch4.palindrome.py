#Largest palindrome product

def palindromic(n):
    s=str(n)
    s1=list(s)
    s2=list(s1)
    s1.reverse()

    if(s1==s2):
        return True
    return False

srch=False
result=0
for i in reversed(range(100,999)):
    for j in reversed(range(100,999)):
        mul=i*j
        if(result > mul):
            break
        if(palindromic(mul)):
            tmp=mul
            if(result<tmp):
                result=tmp
                break
   
print(result)
