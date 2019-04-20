import math

#returns list of all permutations
def perm(linfo):
    ans=[]
    size=len(linfo)

    def permH(slinfo,prev,smallAns):
        if len(slinfo)==1:
            prev.append(slinfo[0])
            smallAns.append(prev)
            print(smallAns)
            return
        i = 0
        smallSize=len(slinfo)
        
        while i<smallSize:
            tempprev=prev[:]
            tempSlinfo=slinfo[:]
            print("slinfo: ",slinfo,",  i: ",i)
            tempprev.append(slinfo[i])
            tempSlinfo.pop(i)
            permH(tempSlinfo,tempprev,smallAns)
            i+=1
        return
        
    
    permH(linfo,[],ans)
    return ans
def permOther(L):
    if len(L)<=1:
        yield L
    else:
        for i in range(len(L)):
            for sp in permOther(L[:i]+L[i+1:]):
                yield [L[1]]+SP


def check(l,perm):
    c1=math.factorial(l)==len(perm)
    return c1==True

a1=perm([0,1,2])
a2=perm([0])
print(a2)
print(a1)
print(check(3,a1))
