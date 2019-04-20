#! /usr/bin/python3

"""Sudoku Project Part 1"""
import sys
import time


def box_id(i,j):#give id of box given i,j
    if j<=2:
        return int(i/3)
    if j>=6:
        return 6+int(i/3)
    return 3+int(i/3)   


"""  fill board"""
def naiiveSolve(problem):

    cliques_rows=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
    cliques_columns=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
    cliques_boxes=[set(),set(),set(),#j:0-2;
                   set(),set(),set(),
                   set(),set(),set()]
    empty={}#dictionary of empty entries and their respective potential numbers

    counter=[0]#id for removing stuff
    
    '''fill cliques'''
    i = 0
    while i < 9:
        j=0
        while j<9:
            if problem[i][j]!='_':
                num=int(problem[i][j])
                cliques_rows[i].add(num)
                cliques_columns[j].add(num)
                cliques_boxes[box_id(i,j)].add(num)
            else:
                empty[(i,j)]=set()
            j+=1
        i+=1
    del i

    def possibles(i,j):#variables:i,j,allNum
        #return set of possibles in i,j
        allNum={1,2,3,4,5,6,7,8,9}
        allNum2=allNum-cliques_rows[i]-cliques_columns[j]-cliques_boxes[box_id(i,j)]
        empty[(i,j)]=allNum2
        return allNum2
        
    def possUpdate(champ=None):
        # we want to find the box with the least number of possibles
        if len(list(empty.keys()))==0:
            print('exhausted empty.keys()')
            return True,True,True
        for k in list(empty.keys()):

            allNum=possibles(k[0],k[1])
            if not champ:
                champ=(k[0],k[1],len(allNum))
            updateCount=0
            if len(allNum)<=champ[2] and len(allNum)!= 0:
                #most likely next update
                champ=(k[0],k[1],len(allNum))
                updateCount+=1

            if updateCount==0 and len(allNum)==0:#deadend
                return False,False,False
        if fillForced()!=0:
            #if fill forced says that it did an update, perhaps the new information need to be put in
            champ=possUpdate()
        return champ

    history = Stack()#stack of all past updates
    higherAuthority=set()
    
    def fillForced():
        numUpdate=0
        K=list(empty.keys())
        #list of places where it has not been filled yet
        #list to prevent the removal of some key from interfering
        for k in K:
            if k not in higherAuthority:
                possibles(k[0],k[1])#update number of possibles of current cell

                if len(empty[k])==1:#only one option
                    addNumber(list(empty[k])[0],k[0],k[1],True)
                    numUpdate+=1
                
        return numUpdate
            
    def addNumber(n,i,j,deed):
        if  deed==True:#add number
            cliques_rows[i].add(n)
            cliques_columns[j].add(n)
            cliques_boxes[box_id(i,j)].add(n)
            problem[i][j]=str(n)
            
            empty.pop((i,j))#added, so not empty anymore
            history.push([i,j,n,counter[0]])
            return
        elif deed==False:#remove number
            quiad = history.pop()#[i,j,n,id]

            c=quiad[3]
            #print('backtracking c',c)
            while quiad and quiad[3]==c:#pop everything with counter=first counter
                remove(quiad[0],quiad[1],quiad[2])
                quiad=history.pop()

            history.push(quiad)
            
        return 
    def remove(x,y,n):
        cliques_rows[x].remove(n)
        cliques_columns[y].remove(n)
        cliques_boxes[box_id(x,y)].remove(n)
        possibles(x,y)#update possibles of that entry
        problem[x][y]='_'
        return

    def search(backtrack_counter=None):
        if not backtrack_counter:
            backtrack_counter=[0]

        i,j,k=possUpdate()
        #possUpdate gives the most probable updaate

        if i==True and isinstance(i,bool):#exhausted empty
            #print(i,j,k)
            #print(empty)
            print(backtrack_counter)
            return True

        if i ==False:#deadend, need to backtrack
            
            return False
        #print(empty[(i,j)])
        
        higherAuthority.add((i,j))# we are working on this, so don't want ot be disturbed
        counter[0]+=1
        for poss in list(empty[(i,j)]):
            addNumber(poss,i,j,True)
          
            if search(backtrack_counter):
                return True
            else:
                backtrack_counter[0]+=1
                addNumber(0,0,0,False)

        higherAuthority.remove((i,j))
        return False

    print(search())
    return problem




"""read and interpret sudoku problem"""
def problemRI(whole=False):
    """reading file"""
    fin= open(sys.argv[1],'r')
    lines=fin.read().split('\n')
    fin.close()

    """variables introduction"""
    counter = 0#sudoku takes 9 lines, excluding heading
    header=[]#stores heading
    problem=[]#stores problem
    solved=[]#stores sovled problem
    check=False#sees if solution is correct

    s=''#if need to write file
    
    for line in lines:
        line=line.split(',')
        if counter > 0:#we are currently on a problem
            problem.append(line)
            counter +=1
        if counter < 0:#we are looking at a solution
            problem.append(line)
            counter -=1
        if counter == 10:#finished parsing through problem
            counter = 0
            st=time.time()
            solved = naiiveSolve(problem)#answer problem
            et=time.time()
            print('time',et-st)
            
            problem=[]#reset problem
            header1=header
            header1[2]='solved'
            Solved=liToStr(solved,header1)#csv version of solution
            #Solved=liToStr(solved)#csv version of solution
            s+=Solved+'\n'
            s+='\n'
            print(Solved)
            
        if counter == -10:#finished parsing through solution
            counter = 0
            check = solved==problem#check if answer is correct
            problem=[]#reset
            print(check)

        if len(line)==3:#indicates is a header
            #print(line)
            if not whole:
                if line==sys.argv[3].split(','):
                    header=line
                    counter+=1
            else:
                if line[2]=='unsolved':#problem
                    header=line
                    counter +=1
                elif line[2]=='solved':#solution
                    counter -=1
            
    try:
        fout = open(sys.argv[2],'w')
        fout.write(s)
        fout.close()
    except:
        print('au revoir')

                
        
def liToStr(problem,header=None):
    """geneartes csv from double arrays and header"""
    #print(problem)
    s=''
    if header:
        h=','.join(header)
        s+=h+'\n'
    for line in problem:
        #print(line)
        s+=','.join(line)+'\n'
    return s
    



"""Stack"""
class Stack: #LIFO

    def __init__(self):
        self.stackList=[]
        self.size=0

    def pop(self):
        if self.size==0:
            return None
        else:
            self.size-=1
            return self.stackList[self.size]
                        
    def push(self, item):
        if self.size<len(self.stackList):
            self.stackList[self.size]=item
        else:
            self.stackList.append(item)
            
        self.size+=1
        return

def stacktest():
    stackTrial = Stack()
    i=0
    while i < 10:
        stackTrial.push(i)
        i+=1
    while i >=5:
        print(stackTrial.pop())
        i-=1
    while i < 15:
       stackTrial.push(i)
       i+=2
    while i >=0:
        print(stackTrial.pop())
        i-=1
    return

#problemRI()
problemRI(True)
