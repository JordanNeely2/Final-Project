class Reversi:

    #initialize board with 2 white and 2 black pieces
    def __init__(self):
        self.board = []

        #create board with starting position
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

            self.board.append(line)
        
        self.curr_player = "Black"
        
        self.empty = 60
        self.finished = False
        
        return

    #prints board to screen
    def printBoard(self):
        print()
        print(' ' * 2 + ' '.join(str(i) for i in range(8)))
        for i in range(len(self.board)):
            print(str(i) + ' ' + ' '.join(self.board[i]))
        print()
        return


    #checks if given move is valid
    #TODO: check if play is valid, not just empty spot on board
    def isValidMove(self, move):
       
        r = move["row"]
        c = move["col"]

        if r in range(8) and c in range(8) and self.board[r][c] == '.':
            
            for i in {-1, 0, 1}:
                for j in {-1, 0, 1}:

                    if r + i in range(8) and c + j in range(8):
                        if self.board[r + i][c + j] in {'B', 'W'}:
                            return True

        print("Invalid move, try again.")
        return False


    #read input from player to get move
    #return dictionary containing row and col info
    def getMove(self):
      
        move = input("Enter a move: ")
     
        while len(move.split()) != 2:
            print("Invalid input: usage - row column")
            move = input("Enter a move: ")

        row = int(move.split()[0])
        col = int(move.split()[1])

        return {"row": row, "col": col}


    #play move
    #TODO: flip over appropriate pieces
    def playMove(self, move):
       
        r = move["row"]
        c = move["col"]

        if self.curr_player == "Black": 
            self.board[r][c] = 'B'
        else: 
            self.board[r][c] = 'W'
        
        self.empty -= 1
        if self.empty == 0: self.finished = True

        return

    #switch to next player's turn
    def changePlayer(self):
        if self.curr_player == "Black":
            self.curr_player = "White"
        else:
            self.curr_player = "Black"

        return

    #print whose turn it is
    def printPlayer(self):
        print(f"{self.curr_player}'s turn.\n")

        return
