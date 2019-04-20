#! /usr/bin/python3

"""Word Ladder Assignment"""

import sys
import math
import time


def main():
    L=readfile()
    D=allwords2(len(L[0][0]))
    s=''
    for pair in L:
        t0=time.time()
        ans=process(pair[0],pair[1],D)
        t1=time.time()
        print(t1-t0)
        s+=','.join(ans)+'\n'
        
    fw=open(sys.argv[2],'w')
    fw.write(s)
    fw.close()
    return

def process(start,end,D=None):
    if not D:
        D=allwords2(len(start))
    frontier = Pqueue()
    H_0=num_same(start, end)
    frontier.push([H_0,0,start])#[G+H,G,...]
    explored = set()

    while frontier.peek():
        word_value=frontier.pop()
        if explore_expand(word_value,end,D,frontier,explored):
            print('success!')
            return word_value[2:]
    return [start,end]
    
def readfile():
    L=[]
    fin = open(sys.argv[1],'r')
    fread=fin.read()
    fin.close()
    lines=fread.split('\n')
    for line in lines:
        if line != "":
            od=line.split(',')
            L.append(od)
    return L

def explore_expand(word_value, destination,D,pq,explored):#[value,G,word0,...]
    word=word_value[len(word_value)-1]
    if word in explored:
        return False
    #print(word)
    if word==destination:
        return True
    else:
        neighbours = D[word]
        G=word_value[1]+1
        for neighbor in neighbours:
            if neighbor not in explored:
                J = word_value[:]
                H=num_same(neighbor, destination)
                J[0]=G+H
                J[1]=G
                J.append(neighbor)
                pq.push(J)
    explored.add(word)
    return False

def num_same(word,goal):
    same=len(word)
    i=0
    while i < len(word):
        if word[i]==goal[i]:
            same-=1
        i+=1
    return same
            

def allwords2(n):
    f = open("dictall.txt",'r')
    S={x.strip() for x in f if len(x)==n+1}#set of all 4 char words
    f.close()
    D={}

    def findNeighboursABC(entry):
        alphabet="abcdefghijklmnopqrstuvwxyz"
        D[entry]=[]
        i=0
        while i < len(entry):
            for ch in alphabet:#search of neighbors char by char, faster
                word = entry[:i]+ch+entry[i+1:]
                if word != entry and word in S:
                    D[entry].append(word)
            i+=1
        return
                    
    for a in S:
        findNeighboursABC(a)
    
    return D




class Pqueue:
    
    def __init__(self,compfxn=None):
        self.arr = ['null']
        self.size=0
        if compfxn:
            self.compfunc=compfxn
        else:
            def ordinaryComp(a,b):
                if a[0]<b[0]:
                    return -1
                if a[0]==b[0]:
                    return 0
                return 1
            self.compfunc=ordinaryComp
    
    def switch(self,a,b):
        A=self.arr[a]
        self.arr[a]=self.arr[b]
        self.arr[b]=A
            
    def push(self, data):
        
        self.size+=1#update size
        if len(self.arr)==self.size:#if new size > length, need append
            self.arr.append(data)
        else:
            self.arr[self.size]=data
        
        dataloc=self.size#where data is added
                
        while math.floor(dataloc/2)>0  and self.compfunc(data,self.arr[math.floor(dataloc/2)])==-1:#parent is smaller than data and parent>0
            self.switch(dataloc,math.floor(dataloc/2))
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




main()

