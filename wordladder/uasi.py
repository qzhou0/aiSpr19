#! /usr/bin/python3

"""Post-Word Ladder Assignment"""



def Uasimain():
    S=allwords2()
    L=list(S)
    ans={}
    for word in L:
        neoW=vowelShift(word)
        if neoW in S and neoW!=word:
            if word not in ans.keys():
                ans[neoW]=[word]
            else:
                ans[neoW]=ans[word]
                ans[neoW].append(word)
                ans.pop(word)
                
    print(ans)
    
    return ans

def vowelShift(word):
    V={'a','e','i','o','u'}
    def is_goodY(word,i):
        if i+1>=len(word):
            return True
        if word[i+1] not in V:
            return True
        return False
    i = 0
    current=''
    first=-1
    while i<len(word):
        cha = word[i]
        
        if cha in V or (cha=='y' and is_goodY(word,i)) :
            if first == -1:
                first = i
            else:
                word=word[:i]+current+word[i+1:]
            current = cha
        i+=1
    if first !=-1 and current !='':
        word=word[:first]+current+word[first+1:]
    return word
    


            

def allwords2(n=None):
    f = open("dictall.txt",'r')
    if not n:
        S={x.strip() for x in f}#set of all 4 char words
    else:
        S={x.strip() for x in f if len(x)==n+1}#set of all 4 char words
    f.close()
       
    return S


Uasimain()

def UnivocalicMain():
    n = 1
    ans={}
    v=['a','i','e','o','u','y']
    while n < 20:
        S = allwords2(n)
        L = list(S)
        
        for word in L:
            for vowel in v:
                if orthodox(word, vowel):

                    k = str(n)+vowel
                    if k in ans.keys():
                        ans[k].add(word)
                    else:
                        ans[k]={word}
        n+=1

    K = ans.keys()
    for k in K:
        print(k, len(ans[k]))
    #print(ans)
        
    return ans

def orthodox(word, vowel):
    V={'a','e','i','o','u'}
    v_count=0

    if vowel!='y':
        V.remove(vowel)
    def is_goodY(word,i):
        if i+1>=len(word):#final y
            return True
        if word[i+1] not in V:#y not followed by vowel
            if i==0 or (word[i-1] not in V and word[i-1]!=vowel):#if previous word is not vowel
                return True
        return False
    
    i = 0
    while i<len(word):
        if word[i] in V:
            # if word == "zoo":
            #     print('1'+vowel)
            return False
        if word[i]=='y' and is_goodY(word,i):
            if vowel!='y':
                # if word == 'zoo':
                #    print('2'+vowel) 
                return False
        if word[i]==vowel:
            v_count +=1
        i +=1
    if v_count<1:
        # if word == 'zoo':
        #     print('3'+vowel)
        return False
    return True

UnivocalicMain()
