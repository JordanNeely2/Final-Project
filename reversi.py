#initialize board with 2 white and 2 black pieces
def initBoard():
    board = []

    for i in range(8):
        line = []
        if i not in {3, 4}:
            for j in range(8):
                line.append('.')
        
        else:
            for j in range(8):
                if j not in {3, 4}:
                    line.append('.')
                else:
                    if i == j:
                        line.append('W')
                    else:
                        line.append('B')

        board.append(line)
    return board


#prints board to screen
def printBoard(board):
    print()
    for i in range(len(board)):
        print(' '.join(board[i]))
    print()
    return


#checks if given move is valid
#TODO: check if play is valid, not just empty spot on board
def isValidMove(board, move):
#   original isValid move just incase none of the below works out
#   if move["row"] > 7 or move["col"] > 7: return False
#   if board[move["row"]][move["col"]] == '.': return True                
#   else: return False
  
    r = int(move["row"])
    c = int(move["col"])
    #invalid moves
    if move["row"] > 7 or move["col"] > 7: return False

    #valid moves
    if board[r][c] == '.': 
        if board[r+1][c] in ('W', 'B'): return True    # 1 below
        if board[r-1][c] in ('W', 'B'): return True    # 1 above
        if board[r][c+1] in ('W', 'B'): return True    # 1 right
        if board[r][c-1] in ('W', 'B'): return True    # 1 left
        if board[r+1][c+1] in ('W', 'B'): return True    # up right
        if board[r+1][c-1] in ('W', 'B'): return True    # up left
        if board[r-1][c+1] in ('W', 'B'): return True    # down right
        if board[r-1][c-1] in ('W', 'B'): return True    # down left

    else: return False


#read input from player to get move
def getMove(curr_player):
  
    move = input("Enter a move: ")
  
    row = int(move.split()[0])
    col = int(move.split()[1])

    return {"row": row, "col": col}


#play move
#TODO: flip over appropriate pieces
def playMove(board, move, curr_player):
    
    if curr_player == "Black": board[move["row"]][move["col"]] = 'B'
    else: board[move["row"]][move["col"]] = 'W'
    return

#switch to next player's turn
def changePlayer(curr_player):
    if curr_player == "Black":
        curr_player = "White"
    else:
        curr_player = "Black"

    print(f"{curr_player}'s turn.\n")

    return curr_player
