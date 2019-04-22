class Reversi:
    
    #initialize board with 2 white and 2 black pieces
    def __init__(self):
        self.board = []

        self.piece = {}
        self.piece["Black"] = 'B'
        self.piece["White"] = 'w'

        self.poss_moves = set()

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
                            line.append(self.piece["White"])
                        else:
                            line.append(self.piece["Black"])
            
            for i in range(2, 6):
                for j in range(2, 6):
                    if i not in {3, 4} or j not in {3, 4}:
                        self.poss_moves.add((i, j))

            self.board.append(line)
        
        self.curr_player = "Black"
        
        self.empty = 60

        self.count = {}
        self.count[self.piece["Black"]] = 2
        self.count[self.piece["White"]] = 2
       
        self.valid_moves = {}
        self.valid_moves[self.piece["Black"]] = {}
        self.valid_moves[self.piece["White"]] = {}

        self.finished = False
        
        return



    #prints board to screen
    def printBoard(self, playable=False, filename=None):
        
        if filename == None:
            pfunc = print
        else:
            f = open(filename, 'w')
            pfunc = f.write


        pfunc('')
        if filename == None:
            pfunc("%s" % (' ' * 2 + ' '.join(str(i) for i in range(8))))
        

        curr = self.piece[self.curr_player]
        """if self.curr_player == "Black": curr = self.piece["Black"]
        else: curr = self.piece["White"]
        """
        
        to_print = ""

        for i in range(8):
            if filename == None:
                to_print += str(i) + ' ' * 1
            
            if playable:
                for j in range(len(self.board[i])):
                    if (i, j) in self.valid_moves[curr] and \
                            self.valid_moves[curr][(i, j)]["modified"] == False:

                        to_print += 'o '
                    else:
                        to_print += self.board[i][j] + ' '
            
            else:
                to_print += ' '.join(self.board[i])
                       
            to_print += '\n'

        pfunc(to_print)
        
        pfunc('')

        if filename != None:
            f.close()
        
        return
    


    #writes board to file, default name board.txt
    def writeBoard(self, filename="board.txt"):
        with open('board.txt','w') as f:
            for i in range(8):
                f.write(' '.join(self.board[i]))
                f.write('\n')

        return



    #read input from player to get move
    #return dictionary containing row and col info
    def getMove(self, filename=None):
        
        if filename == None:
            move = input("Enter a move: ")
         
            while len(move.split()) != 2:
                print("Invalid input: usage - row column")
                move = input("Enter a move: ")

        else:
            move = None
            
            while move == None:
                try: 
                    with open('move.txt','r') as f:
                        move = f.read().strip()
                        print(move)
                except FileNotFoundError:
                    None
        print(move.split())
        row = int(move.split()[0])
        col = int(move.split()[1])

        return {"row": row, "col": col}



    #find and store valid moves for each player
    #memoize moves - if no pieces affected are changed, it is still valid
    def findValidMoves(self, player=None):
      
        #print(self.poss_moves)

        if player == None: player = self.curr_player

        if player == "all":
            players = ["Black", "White"]
        else:
            players = [player]

        #print(players)

        for p in players:

            curr = self.piece[p]

            """if p == "Black": curr = self.piece["Black"]
            else: curr = self.piece["White"]
            """

            for move in self.poss_moves:
                if move in self.valid_moves[curr] and \
                self.valid_moves[curr][move]["modified"] == False:
                    continue
                else:
                    #print(f"p: {p}, move: {move}")
                    #print(f"playing move: {move[0]}, {move[1]}")
                    if move in self.valid_moves[curr] and \
                    self.valid_moves[curr][move]["modified"] == True:
                        del self.valid_moves[curr][move]

                    self.playMove({"row": move[0], "col": move[1]}, p, modify=False)
        if len(self.valid_moves[curr]) == 0: self.changePlayer()        
                    
        #print(self.valid_moves[self.piece["Black"]], '\n')
        #print(self.valid_moves[self.piece["White"]])
        return



    #check validity of move and play it
    #return True on valid move, False on invalid
    def playMove(self, move, player=None, modify=True, vis=True):
       
        if player == None: player = self.curr_player

        r = move["row"]
        c = move["col"]
        
        valid = False

        #check if spot is empty and on the board
        if r in range(8) and c in range(8) and self.board[r][c] == '.':
            
            for i in {-1, 0, 1}:
                for j in {-1, 0, 1}:

                    if r + i in range(8) and c + j in range(8):
                        if self.board[r+i][c+j] in {self.piece["Black"], self.piece["White"]}:
                            valid = True
        
        #find and flip opposing pieces
        if (valid):
            num_flipped = 0

            if player == "Black":
                curr = self.piece["Black"]
                opp = self.piece["White"]
            else:
                curr = self.piece["White"]
                opp = self.piece["Black"]
            
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
                                if mul == 1: break 

                                #backtrack and flip pieces
                                for m in range(mul - 1, 0, -1):
                                    if modify:
                                        self.board[r + i * m][c + j * m] = curr
                                        
                                        #check valid moves and mark modified
                                        for player in {curr, opp}:
                                            cand = self.valid_moves[player]
                                            
                                            for mov in cand:
                                                 
                                                if (r+i*m, c+j*m) in \
                                                    cand[mov]["to_flip"]:

                                                    cand[mov]["modified"]=True
                                                elif (r+i*m, c+j*m) in \
                                                        cand[mov]["endpts"]:

                                                    cand[mov]["modified"]=True
                                    else:
                                        if (r, c) not in self.valid_moves[curr]:
                                            self.valid_moves[curr][(r, c)] = {}

                                        cand = self.valid_moves[curr][(r, c)]
                                        
                                        if "to_flip" not in cand:
                                            cand["modified"] = False
                                            cand["to_flip"] = set()
                                            cand["count"] = 0
                                        
                                        cand["to_flip"].add((r+i*m, c+j*m))
                                        cand["count"] += 1

                                    num_flipped += 1
                                
                                if not modify:
                                    cand = self.valid_moves[curr][(r,c)]

                                    if "endpts" not in cand:
                                        cand["endpts"] = set()

                                    cand["endpts"] |= {(r+i*mul,c+j*mul)}
                                
                                break
                            else: break

            #if no pieces flipped, invalid move, else place piece for turn
            if (num_flipped == 0):
                valid = False   
            else:

                if modify:
                    self.board[r][c] = curr
                    #self.last_played = (r, c)

                    self.empty -= 1
                    if self.empty == 0: self.finished = True

                    self.count[curr] += num_flipped + 1
                    self.count[opp] -= num_flipped

                    #TODO: modify poss_moves
                    self.poss_moves -= {(r, c)}

                    for i in {-1, 0, 1}:
                        for j in {-1, 0, 1}:
                            if i == 0 and j == 0:
                                continue
                            
                            self.poss_moves |= {(r+i,c+j)}

                    for player in {curr, opp}:
                        cand = self.valid_moves[player]

                        if (r, c) in cand:
                            del cand[(r,c)]                        

                else:
                    None
                    #TODO: code to check a move 

        if not valid and modify and vis:
            print("Invalid move, try again.")

        return valid



    #switch to next player's turn
    def changePlayer(self):
        curr = self.curr_player
        if self.curr_player == "Black":
            opp = "White"
        else:
            opp = "Black"

        if len(self.valid_moves[self.piece[curr]]) != 0:
            self.curr_player = opp
            
        return



    #print whose turn it is
    def printPlayer(self):
        
        if self.empty > 0: print("%s's turn.\n" % (self.curr_player))
        else: print("Game is finished!")
        return


    #print score
    def printScore(self):
        print("Black: %s" % ({self.count[self.piece['Black']]}))
        print("White: %s\n" % ({self.count[self.piece['White']]}))
        return
