#! /usr/bin/python3

"""Pre-WordLadder Assignment"""

import sys

#import time


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
    
    #print(D)
    return D
#allwords2(4)

def in_process(inputwords):
    """
    inputwords is list of wordlist of input file
    """
    fin=open(sys.argv[1],'r')
    lines=fin.read().split('\n')
    fin.close()
    for line in lines:
        if line!="":
            inputwords.append(line)
    return

def out_process(s):
    fout=open(sys.argv[2],'w')
    fout.write(s)
    fout.close()
    return

def stuffToDo():
    #t0=time.time()
    Linputs=[]
    in_process(Linputs)
    n=len(Linputs[0])

    D=allwords2(n)
    s=''
    for k in Linputs:
        s+=k+','+str(len(D[k]))+'\n'

    out_process(s)
    #t1=time.time()
    #print(t1-t0)

    return

stuffToDo()



''' old method
def allwords(n):
    """
    n is character length
     """
    fword = open("dictall.txt",'r')
    lines=fword.read().split('\n')
    fword.close()
    
    D={}
    for line in lines:
        if len(line)==n:
            D[line]=[]
            findNeighbours(line,D)
    #findNeighborsAlphabet(D)--too long
    return D
'''
'''
def findNeighbours(entry,D):

    def isNeighbor(w1,w2):
        if w1==w2:
            return False
        diff=0
        i = 0
        while i < len(w1):
            if w1[i]!=w2[i]:
                diff+=1
            i+=1
        if diff==1:
            return True
        """n = len(w1)-1
        while n>=0:
            if w1[:n]+w1[n+1:]==w2[:n]+w2[n+1:]:
                return True
            n-=1
        """
        return False
        
    keys=D.keys()
    se=set(entry)

    critical_num=len(entry)-1+len(se)-len(entry)
    
    for key in keys:
        temp_critNum=critical_num
        sk=set(key)
        #print(se,' : ',sk,' : ',sk.intersection(se))
        temp_critNum=temp_critNum+len(sk)-len(key)

        if len(sk.intersection(se))>=temp_critNum:
            
            if key!=entry and isNeighbor(key,entry):
                D[key].append(entry)
                D[entry].append(key)
    return
'''
