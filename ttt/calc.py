
def counter():
    x=0
    def count():
        nonlocal x
        x+=1
        return x
    def show():
        return x
    return count, show
    

game_counter,gs=counter()
board_counter,bs=counter()
draw_counter,ds=counter()
Xwin_counter,xs=counter()


allBoards=set()
allirrBoards=set()
endBoards=set()

board0=[0,0,0,0,0,0,0,0,0]
empty0={0,1,2,3,4,5,6,7,8}
player=1

Xwinboards=[]

def check(board,empty):
    if (board[0]==board[1]==board[2] or board[0]==board[3]==board[6] or board[0]==board[4]==board[8]) and board[0]!=0:
        return board[0]
    elif (board[3]==board[4]==board[5] or board[1]==board[4]==board[7] or board[2]==board[4]==board[6]) and board[4]!=0:
        return board[4]
    elif (board[6]==board[7]==board[8] or board[2]==board[5]==board[8]) and board[8]!=0:
        #print (board[8])
        return board[8]
    if len(empty)==0:
        return -10
    return 0
"""--------------------------"""
def flip3(board):
    return [board[2],board[5],board[8],board[1],board[4],board[7],board[0],board[3],board[6]]
def isDup3(board,g):
    i=0
    board=[str(i) for i in board]
    while i <9:
        if board[i]=='0':
            board[i]='_'
        elif board[i]=='1':
            board[i]="x"
        else:
            board[i]='o'
        i+=1
    i=0
    while i<4:
        i+=1
        board=flip(board)
        if ''.join(board) in g:
            return
    g.add(sboard)
    return
"""----------------------------------"""
def flip(board):
    return [board[2],board[5],board[8],
            board[1],board[4],board[7],
            board[0],board[3],board[6]]
def transpose(board):
    return [board[0],board[3],board[6],
            board[1],board[4],board[7],
            board[2],board[5],board[8]]
def reflect(board):
    return [board[8],board[5],board[2],
            board[7],board[4],board[1],
            board[6],board[3],board[0]]
def isDup(board,g):
    i=0
    while i<6:
        i+=1
        board=flip(board)
        tboard=transpose(board)
        rboard=reflect(board)
        if str(board) in g or str(tboard) in g or str(rboard) in g:
            return
    g.add(str(board))
    
    return



def play(board,empty,player):
    
    state=check(board,empty)
    if state == -1:
        game_counter()
        isDup(board,endBoards)
        #print(board)
        return
    elif state==1:
        game_counter()
        Xwin_counter()
        isDup(board,endBoards)
        Xwinboards.append(str(board))
        #print(board)
        return
    elif state==-10:
        game_counter()
        draw_counter()
        isDup(board,endBoards)
        #print(board)
        return
    else:
        for loc in empty:
            b=board.copy()
            e=empty.copy()
            
            b[loc]=player
            e.remove(loc)

            board_counter()
            allBoards.add(str(b))
            isDup(b,allirrBoards)
            
            play(b,e,player*-1)
    return

play(board0,empty0,player)

print('game_counter: ',gs())#255168
print('draw_counter: ',ds())# 46080
print('Xwin_counter: ',xs())#131184, so 77904 wins by O
print('board_counter:',bs())#549945
print(len(allBoards))#5477+1 (didn't count first board)
print(len(allirrBoards))#764+1
print(len(endBoards))#245
# for b in allirrBoards:
#     b=b[1:len(b)-1]
#     b=b.split(',')
#     print(str(b[:3])+'\n'+str(b[3:6])+'\n'+str(b[6:]))
#     print('--------------------------------')
    
print('xwinboards',len(Xwinboards))
print(len(set(Xwinboards)))
