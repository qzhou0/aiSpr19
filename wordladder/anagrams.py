#! /usr/bin/python3

"""Anagrams"""

import sys


def readdict():
    D={}
    f = open("dictall.txt",'r')
    for x in f:
        word=x.strip()
        #print(word)
        lw=list(word)
        lw.sort()
        lsword=''.join(lw )
        if lsword not in D.keys():
            D[lsword]=[word]
        else:
            D[lsword].append(word)
        
    f.close()

    keys=D.keys()
    for key in keys:
        if len(D[key])>3:
            print(key,len(D[key]),D[key])
    
    return D

    
readdict()

#7, ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])
