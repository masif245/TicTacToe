def welcomeMessage():
    print ('Hello !!! Welcome to the tic tac toe game.')
    
#clear = lambda: os.system('clear')

def clear(): 
    clr = "\n" * 100
    print (clr)
    
def getPlayedChoice():
    Player1 = input('Hey Player 1 ! Enter your choice of character X/O: ')
    
    while (Player1 != 'X' and Player1 != 'O'):
        Player1 = input('Hey Player 1 ! Enter your choice of character X/O: ')
    #else:
    #    break
        
    if Player1 == 'X':
        Player2 = 'O'
    else:
        Player2 = 'X'
        
    return Player1, Player2

def displayBoard(board):
    clear()
    print ('\t    |    |    ')
    print ('\t  {}  | {}   |  {}  '.format(board[0], board[1], board[2]))
    print ('\t____|____|____')
    print ('\t    |    |    ')
    print ('\t  {}  | {}   |  {}  '.format(board[3], board[4], board[5]))
    print ('\t____|____|____')
    print ('\t    |    |    ')
    print ('\t  {}  | {}   |  {}  '.format(board[6], board[7], board[8]))
    print ('\t    |    |    ')

def validate(board, idx):
    if board[idx-1] != 'X' and  board[idx-1] != 'O':
        return True

def getUserInput(plnum,board):
    val = input('Hey Player {} make your move (Enter poistion 1-9): '.format(plnum))
    if validate(board, int(val)):
        return int(val)
    else:
        return False
        
    
def wincheck(board,pnum):
    
    if len(board)<3:
        return False
    else:
        if (board[0]==board[1]==board[2]==pnum) or (board[3]==board[4]==board[5]==pnum) or (board[6]==board[7]==board[8]==pnum) or (board[0]==board[3]==board[6]==pnum) or (board[1]==board[4]==board[7]==pnum) or (board[2]==board[5]==board[8]==pnum)or (board[0]==board[4]==board[8]==pnum) or (board[2]==board[4]==board[6]==pnum):
            return True
        else:
            return False

def main():

    move = ''
    ii = ''
    welcomeMessage()
    board = ['']*9
    Player1, Player2 = getPlayedChoice()
    print('Players your representation is  Player 1-> {}  Player 2-> {}'.format(Player1,Player2))
    print('Lets Begin. Here is the empty board...')
    displayBoard(board)
    
    for ii in range(1,10):
        if ii % 2 == 0:
            move = getUserInput('2', board)
            
            while (move == False):
                print('Hey you cant cheat choose another index')
                move = getUserInput('2', board)
                
            board[move-1] = Player2
            displayBoard(board)
            if wincheck(board, Player2)==True:
                print ('Player 2 wins')
                break
        else:
            move = getUserInput('1', board)
            
            while (move == False):
                print('Hey you cant cheat choose another index')
                move = getUserInput('2', board)
                
            board[move-1] = Player1
            displayBoard(board)
            if wincheck(board, Player1)==True:
                print ('Player 1 wins')
                break
           
    if wincheck(board, Player1) == False and wincheck(board, Player2) == False:
        print('\n Hehehehehehhehe Match Draw')

if __name__ == '__main__':
    main()

