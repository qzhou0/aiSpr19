#! /usr/bin/python 

import math

class Pqueue:
    
    def __init__(self,compfxn=None):
        self.arr = ['null']
        self.size=0
        if compfxn:
            self.compfunc=compfxn
        else:
            def ordinaryComp(a,b):                
                if a<b:
                    return -1
                if a==b:
                    return 0
                return 1#a>b
            self.compfunc=ordinaryComp
            
    
    def switch(self,a,b):
        A=self.arr[a]
        self.arr[a]=self.arr[b]
        self.arr[b]=A
        #print(self.arr[a])
    
    def push(self, data):
        
        self.size+=1#update size
        if len(self.arr)==self.size:#if new size > length, need append
            self.arr.append(data)
        else:
            self.arr[self.size]=data
        
        dataloc=self.size#where data is added
        #floor(n/2)=parent
        
        while math.floor(dataloc/2)>0  and self.compfunc(data,self.arr[math.floor(dataloc/2)])==-1:#parent is smaller than data and parent>0
                         
            #print("this",data," : ",dataloc,"peak: ",self.arr[1])
            
            self.switch(dataloc,math.floor(dataloc/2))
            #print("post switch: ",self.arr[1])
            dataloc = math.floor(dataloc/2)
           
        
    def mymin(self,a,b,n):
        #if True, means need switch; else stop
        #assume b>a
        if a>b:#switch if not
            newA = b
            b=a
            a=newA
        
        if (a>self.size  and b>self.size) or n>=self.size:
            return False,-1
        elif b>self.size:
            champ = a
        else:
            comp =  self.compfunc(self.arr[a],self.arr[b])
            if comp==-1:#arr[a]<arr[b]
                champ=a
            elif comp ==0:#arr[a]=arr[b],go with smaller one
                champ=a
            else:#arr[b]<arr[a]
                champ=b

        comp=self.compfunc(self.arr[champ],self.arr[n])
        if comp==-1:#stuff at champ is smaller than stuff at n
            return True,champ
        else:
            return False,-1
    
    def pop(self):
        if self.size ==0:#cannot pop if is empty
            return
        
        self.switch(1,self.size)#make first element last element,last first
        self.size-=1
        
        n = 1
        switch,toswitch = self.mymin(2*n,2*n+1,n)
        while switch:
            self.switch(n,toswitch)
            n=toswitch
            switch,toswitch = self.mymin(2*n,2*n+1,n)
        return self.arr[self.size+1]#stuff popped out
        
    def peek(self):
        if self.size ==0:
            return None
        return self.arr[1]
        
    def tolist(self):
        s=self.size
        return [self.pop() for i in range(s)]

#testing

def my_cmp(a,b):
   if len(a) < len(b): 
      return -1
   if len(a) == len(b): 
      return 0
   return 1
  
Fred = Pqueue(my_cmp)

Fred.push([2,"hello",[4,3]])
Fred.push([98.33])
Fred.push(["Why not?","...because"])
print (Fred.peek())
#  [98.33]
print (Fred.pop())
#  [98.33]
print (Fred.pop())
#  ["Why not?, "...because"]
print (Fred.pop())
#  [2, "hello", [4, 3]]
print (Fred.pop())
#  None

Fred.push([2,"hello",[4,3]])
Fred.push([98.33])
Fred.push(["Why not?","...because"])
print(Fred.tolist())

N = Pqueue()
for i in range(100,800):
    N.push(i)
    #print(i,":",N.peek())
for i in range(0,900):
    N.push(i)
    #print(i,":",N.peek())

print(N.peek())
print(N.pop())
s = N.size
for i in range(0,s):
    print(N.pop(),":",N.peek())
