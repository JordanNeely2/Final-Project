class Reversi:

    
    #initialize board with 2 white and 2 black pieces
    def __init__(self):
        self.board = []

        self.b_piece = 'B'
        self.w_piece = 'w'
        
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
                            line.append(self.w_piece)
                        else:
                            line.append(self.b_piece)

            self.board.append(line)
        
        self.curr_player = "Black"
        
        self.empty = 60
        self.b_count = 2
        self.w_count = 2
        self.finished = False
        
        return

    #prints board to screen
    def printBoard(self):
        print()
        print(' ' * 2 + ' '.join(str(i) for i in range(8)))
        for i in range(8):
            print(str(i) + ' ' + ' '.join(self.board[i]))
        print()
        return

    """
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
    """

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
    def playMove(self, move, modify=True):
       
        r = move["row"]
        c = move["col"]
        
        valid = False

        #check if spot is empty and on the obard
        if r in range(8) and c in range(8) and self.board[r][c] == '.':
            
            for i in {-1, 0, 1}:
                for j in {-1, 0, 1}:

                    if r + i in range(8) and c + j in range(8):
                        if self.board[r+i][c+j] in {self.b_piece, self.w_piece}:
                            valid = True
        
        #find and flip opposing pieces
        if (valid):
            num_flipped = 0

            if self.curr_player == "Black":
                curr = self.b_piece
                opp = self.w_piece
            else:
                curr = self.w_piece
                opp = self.b_piece
            
            #check in 8 directions
            for i in {-1, 0, 1}:
                for j in {-1, 0, 1}:

                    #multiply i and j by mul to move across the board in lines
                    for mul in range(1, 8):
                        if r + i * mul in range(8) and c + j * mul in range(8):
                            
                            #keep going until you find a friendly piece
                            if self.board[r + i * mul][c + j * mul] == opp:
                                continue
                            if self.board[r + i * mul][c + j * mul] == curr:
                                
                                #backtrack and flip pieces
                                for m in range(mul - 1, 0, -1):
                                    if modify:
                                        self.board[r + i * m][c + j * m] = curr
                                    else:
                                        None
                                    num_flipped += 1
                                break
                            else: break

            #if no pieces flipped, invalid move, else place piece for turn
            if (num_flipped == 0):
                valid = False   
            else:

                self.board[r][c] = curr

                self.empty -= 1
                if self.empty == 0: self.finished = True

                if self.curr_player == "Black": 
                    self.b_count += num_flipped + 1
                    self.w_count -= num_flipped
                else:
                    self.w_count += num_flipped + 1
                    self.b_count -= num_flipped
                

        if (not valid):
            print("Invalid move, try again.")

        return valid

    #switch to next player's turn
    def changePlayer(self):
        if self.curr_player == "Black":
            self.curr_player = "White"
        else:
            self.curr_player = "Black"

        return

    #print whose turn it is
    def printPlayer(self):
        
        if self.empty > 0: print(f"{self.curr_player}'s turn.\n")
        else: print("Game is finished!")
        return

    def printScore(self):
        print(f"Black: {self.b_count}")
        print(f"White: {self.w_count}\n")
        return
