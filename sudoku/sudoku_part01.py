#! /usr/bin/python3

"""Sudoku Project Part 1"""
import sys
import time





""" naiive fill board"""
def naiiveSolve(problem):
    def box_id(i,j):#give id of box given i,j
        if j<=2:
            return int(i/3)
        if j>=6:
            return 6+int(i/3)
        else:
            return 3+int(i/3)
        
    #print(problem)
    cliques_rows=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
    cliques_columns=[set(),set(),set(),set(),set(),set(),set(),set(),set()]
    cliques_boxes=[set(),set(),set(),#j:0-2;
                   set(),set(),set(),
                   set(),set(),set()]
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

            j+=1
        i+=1
        
    def clique_check():#diagnostic use
        print(cliques_boxes)
        print(cliques_columns)
        print(cliques_rows)
        return
    #clique_check()
    
    history = Stack()
    
    def addNumber(n,i,j,deed):
        if problem[i][j]=='_' and deed==True:#add number
            '''fill cliques'''
            cliques_rows[i].add(n)
            cliques_columns[j].add(n)
            cliques_boxes[box_id(i,j)].add(n)
            '''write in problem'''
            problem[i][j]=str(n)
            '''commit to history'''
            #[print (','.join(line)) for line in problem]
            #print('\n')
            history.push([i,j,n])
            
        elif deed==False:#remove number
            '''this version did not work'''
            triad = history.pop()#[i,j,n]
            #print(triad)
            i = triad[0]
            j=triad[1]
            n = triad[2]
            
            '''remove cliques'''
            cliques_rows[i].remove(n)
            cliques_columns[j].remove(n)
            cliques_boxes[box_id(i,j)].remove(n)
            '''new empty space in problem'''
            problem[i][j]='_'
        return
    
    
    def search(i,j,backtrack_counter=None,direction=None):
        if not backtrack_counter:
            backtrack_counter=[0]
        if i == 9:#exceeded maximum i, so the problem is solved
            print('top')
            print('backtrack counter: ', backtrack_counter)
            return True
        
        """next values"""
        nextj=j+1#moving horizontally
        nexti=i
        if j == 8:#if reached end of row, move on to next row
            nextj=0
            nexti=i+1

        
        if problem[i][j]=='_':#we have to fill this spot
            n=1
            while n <=9:#nine possible numbers
                
                if n not in cliques_rows[i] and n not in cliques_columns[j] and n not in cliques_boxes[box_id(i,j)]:#filter bad ns
                    #print(n)

                    addNumber(n,i,j,True)#add to history

                    if search(nexti, nextj,backtrack_counter):#try it out
                        return True#works!
                    else:#does not work, remove
                        backtrack_counter[0]+=1
                        addNumber(0,0,0,False)
                n+=1#update n
            #print('give up')
            return False#no number completed problem
        else:
            return search(nexti,nextj,backtrack_counter)#spot already filled, moving on
    
    search(0,0)#start from 0,0
    #print('here')
    
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
            print(et-st)
            problem=[]#reset problem
            header1=header
            header1[2]='solved'
            #Solved=liToStr(solved,header1)#csv version of solution
            Solved=liToStr(solved,header1)#csv version of solution
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
