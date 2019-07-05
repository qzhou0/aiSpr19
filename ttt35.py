#! /usr/bin/env python3

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''

import random, sys

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode


class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None
        self.parents = [] 
        self.children = []
        self.best_move = None 
        self.moves_to_end =None 
        self.finalState =None  

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('parents:',self.parents)
        print ('children:',self.children)
        print ('finalState:',self.finalState)

def isWin(layout):

    for comb in Wins:
        if layout[comb[0]]==layout[comb[1]]==layout[comb[2]] and layout[comb[0]]!='_':
            return layout[comb[0]]
    if layout.count('_')==0:
        return 'd'
    return None
        
def detplayer(layout):
    xs=layout.count('x')
    os=layout.count('o')
    if xs==os:
        player='x'
    else:
        player='o'
    return player    
    
def CreateAllBoards(layout,parent):
    if layout in AllBoards.keys():
        if parent not in AllBoards[layout].parents:
            AllBoards[layout].parents.append(parent)
            parent.children.append(AllBoards[layout])
        return 
    given=BoardNode(layout)
    AllBoards[layout]=given
    if parent:
        given.parents.append(parent)
        parent.children.append(given)
    if isWin(layout):
        given.endState=isWin(layout)
        return
    i=0
    player=detplayer(layout)
    while i<9:
        if layout[i]=='_':
            child=layout[:i]+player+layout[i+1:]
            CreateAllBoards(child,given)
        i+=1
    return
CreateAllBoards('_________',None)
#print(len(AllBoards))#5478

def compBoards(lay1,lay2):
    return [i for i in range(9) if lay1[i]!=lay2[i] ][0]

# Socialization of Nodes
def soc(layout):
    given=AllBoards[layout]
    if given.endState:
        #print('end filled')
        given.finalState=given.endState
        given.best_move=[-1]
        given.moves_to_end=0
        return
    player=detplayer(layout)
    #print(player)
    #recursion
    i=0
    champ=[[],None,None]#[id,winner,moves_to_end,]
    while i < len(given.children):
        child=given.children[i]
        soc(child.layout)
        if not champ[0]:#initiation
            champ[0].append(compBoards(layout,child.layout))
            champ[1]=child.finalState
            champ[2]=child.moves_to_end+1
        
        elif champ[1]==player:#winning is possible
            if child.finalState==player:#a win
                if child.moves_to_end+1<champ[2]:#faster win
                    champ[2]=child.moves_to_end+1
                    champ[0]=[compBoards(layout,child.layout)]
                elif child.moves_to_end+1==champ[2]:#equally good
                    champ[0].append(compBoards(layout,child.layout))
        
        elif champ[1]=='d':#drawing is possible
            if child.finalState==player:#this is a win
                champ[2]=child.moves_to_end+1
                champ[1]=player
                champ[0]=[compBoards(layout,child.layout)]
            elif child.finalState=='d':
                if child.moves_to_end+1>champ[2]:#longer game
                    champ[2]=child.moves_to_end+1
                    champ[0]=[compBoards(layout,child.layout)]
                elif child.moves_to_end+1==champ[2]:
                    champ[0].append(compBoards(layout,child.layout))
        
        else:#not win nor draw, lose
            if child.finalState!=player and child.finalState!='d':#this is no win nor draw:
                if child.moves_to_end+1>champ[2]:#longer gae
                    champ[2]=child.moves_to_end+1
                    champ[0]=[compBoards(layout,child.layout)]
                elif child.moves_to_end+1==champ[2]:
                    champ[0].append(compBoards(layout,child.layout))
                    champ[0]=[compBoards(layout,child.layout)]
            else:#this is a win or draw
                champ[2]=child.moves_to_end+1
                champ[1]=child.finalState
                champ[0]=[compBoards(layout,child.layout)]
        i+=1
    given.best_move=champ[0]
    sampleBest=champ[0][0]
    childL=layout[:sampleBest]+player+layout[sampleBest+1:]
    given.moves_to_end = AllBoards[childL].moves_to_end+1 
    given.finalState=AllBoards[childL].finalState
        
    return

#soc('_________')
AllBoards['_________'].finalState='d'
AllBoards['_________'].best_move=[i for i in range(8)]
AllBoards['_________'].moves_to_end=8

row_dict={0:'left',1:'center',2:'right'}
col_dict={0:'upper',1:'middle',2:'lower'}

def bestMove(layout):
    player=detplayer(layout)
    board=AllBoards[layout]
    best=random.choice(board.best_move)
    print(best)
    s=''
    #s+='move='+str(9-layout.count('_')+1)+'\nBest move: '
    s+='move= '+str(best)+'\nBest move: '
    if best==-1:
        s+='game has ended\n'
    else:
        s+=col_dict[int(best/3)]+'-'+row_dict[best%3]+'.\n'

    if board.finalState!= 'd':
        s+=board.finalState +' wins in '+str(board.moves_to_end)+' moves.'
    else:
        s+='Draw in '+str(board.moves_to_end)+' moves.'
    return s
 

def main():
    d={}
    for arg in sys.argv:
        split_arg=arg.split('=')
        if len(split_arg)>1:
            d[split_arg[0]]=split_arg[1]

    s=d['result_prefix']+'\n'

    if 'id' in d.keys():
        s+='author=ttt35.py\n'
        s+='title=ttt35.py\n'
    elif 'board' in d.keys():
        print(d['board'])
        if d['board']!='_________':
            soc(d['board'])
        s+=bestMove(d['board'])
    if 'result_file' in d.keys():
        f=open(d['result_file'],'w')
        f.write(s)
        f.close()
    else:
        print(s)
        
main()        
    
    
