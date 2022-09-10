def p1p2():
    p=[]
    while True:
        p1=input('choose for player1(x or o):')
        if p1 not in ['x','o']:
          print('choose from (x or o) only')
          continue
        else:
            break
    while True:
        p2=input('choose for player2(x or o):')
        if p2 not in ['x','o']:
          print('choose from (x or o) only')
          continue
        if p2 == p1:
            print('choose different value for player2')
            continue
        else:
            break
    p.append(p1)
    p.append(p2)
    return p

def changeboard(pos,brd,player):
    if pos==1:
        brd[31]=player
    elif pos==2:
        brd[33]=player
    elif pos==3:
        brd[35]=player
    elif pos==4:
        brd[17]=player
    elif pos==5:
        brd[19]=player
    elif pos==6:
        brd[21]=player
    elif pos==7:
        brd[3]=player
    elif pos==8:
        brd[5]=player
    elif pos==9:
        brd[7]=player

def checkwin(bord):
    if (((bord[3] == bord[5] == bord[7]) and bord[7] != ' ') or ((bord[17] == bord[19] == bord[21]) and bord[21] != ' ') or ((bord[31] == bord[33] == bord[35]) and bord[35] != ' ') or ((bord[3] == bord[17] == bord[31]) and bord[31] != ' ') or ((bord[5] == bord[19] == bord[33]) and bord[33] != ' ') or ((bord[7] == bord[21] == bord[35]) and bord[35] != ' ') or ((bord[3] == bord[19] == bord[35]) and bord[35] != ' ') or ((bord[7] == bord[19] == bord[31]) and bord[31] != ' ')):
        return True


def checkdraw(b):
    x=[b[3],b[5],b[7],b[17],b[19],b[21],b[31],b[33],b[35]]
    n=0
    for i in x:
        if i!=' ':
            n=n+1
        if n==9:
            return True



def inchoice(p,brd):
    turn=1
    posvalid=[1,2,3,4,5,6,7,8,9]
    posarr=[]
    while True:
        x = checkwin(brd)
        if x == True:
            print('player1 wins')
            break
        d = checkdraw(brd)
        if d == True:
            print('the game is draw')
            break
        else:
            if (turn == 1):
                valid = False
                while not valid:
                    try:
                        pos = int(input('player1:'))
                        valid = True
                    except ValueError:
                        print('enter only numbers')

                if (pos in posarr) or (pos not in posvalid):
                    print('choose proper index')
                    continue
                changeboard(pos, brd, p[0])
                posarr.append(pos)
                turn = 2
                print(*brd, sep='')
                continue
            elif turn == 2:
                valid = False
                while not valid:
                    try:
                        pos = int(input('player1:'))
                        valid = True
                    except ValueError:
                        print('enter only numbers')
                if pos in posarr:
                    print('choose proper index')
                    continue
                changeboard(pos, brd, p[1])
                posarr.append(pos)
                turn = 1
                print(*brd, sep='')
                y = checkwin(brd)
                if y == True:
                    print('player2 wins')
                    break
                continue





def startgame(p,brd):
    print('player1 goes first')
    p1=p
    brd1=brd
    inchoice(p1,brd1)



board=['   |   |   ','\n',' ',' ',' | ',' ',' | ',' ',' ','\n','   |   |   ','\n','-----------','\n','   |   |   ','\n',' ',' ',' | ',' ',' | ',' ',' ','\n','   |   |   ','\n','-----------','\n','   |   |   ','\n',' ',' ',' | ',' ',' | ',' ',' ','\n','   |   |   ']
brd=board.copy()
P=p1p2()
startgame(P,brd)

