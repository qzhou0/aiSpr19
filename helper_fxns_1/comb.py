import time

def comb(L,n):

    if (n==1):
        return L
    A=[]
    i=0
    while i<len(L):
        for elem in comb(L[i+1:],n-1):
            A.append(L[i]+elem)
        i+=1
    return A

t0=time.time()
print(comb(['a','b','c','d'],3))
t1=time.time()
print(t1-t0)
    
