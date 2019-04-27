import reversi as rv
import copy
import random
import time

levels = 5

class ReversiAI:


    def __init__(self, game, level):
        self.game = game
        self.level = level
        
        if self.level in {4, 5}:
            with open('board_weight.txt', 'r') as f:
                self.weights = []

                for line in f:
                    L = []
                    for weight in line.split():
                        L.append(int(weight))

                    self.weights.append(L)

    def getMove(self, level):
        t_start = time.clock()

        wait_time = 1
        
        if level == 1:
            move = self.getMoveRandom()

        if level == 2:
            move = self.getMoveMinMoves()
        
        if level == 3:
            move = self.getMoveMaxScore()

        if level == 4:
            move = self.getMoveWeighted()
        
        if level == 5:
            move = self.getMoveWeighted(k=3)

        t_end = time.clock()

        if t_end - t_start < wait_time:
            time.sleep(wait_time - (t_end - t_start))

        return move

    #return a random valid move
    def getMoveRandom(self):
        move_list = []

        for move in self.game.valid_moves[self.game.piece["White"]]:
            move_list.append(move)
        
        rand_move = random.choice(move_list)
            
        return {"row": rand_move[0], "col": rand_move[1]}


    #returns move with highest score for white after k moves
    def getMoveMaxScore(self, k=1):

        subgames = {}

        for move in self.game.valid_moves[self.game.piece["White"]]:
            for i in range(k):
                subgames[move] = copy.deepcopy(self.game)
                subgames[move].playMove({"row": move[0], "col": move[1]}, "White", modify=True)

        #print(subgames)

        max_score = 0

        for move in subgames:
            
            if subgames[move].count[self.game.piece["White"]] > max_score:
                max_score = subgames[move].count[self.game.piece["White"]]
                best_move = move
        
        return {"row": best_move[0], "col": best_move[1]}


    #return move which minimizes opponent's options after k moves
    def getMoveMinMoves(self, k=1):

        subgames = {}

        for move in self.game.valid_moves[self.game.piece["White"]]:
            subgames[move] = copy.deepcopy(self.game)
            subgames[move].playMove({"row": move[0], "col": move[1]}, "White", modify=True)

        min_moves = 65

        for move in subgames:
            subgames[move].findValidMoves("Black")
            
            n_moves = len(subgames[move].valid_moves[self.game.piece["Black"]])
            if n_moves < min_moves:
                min_moves = n_moves
                best_move = move

        return {"row": best_move[0], "col": best_move[1]}


    #return move with best weighting based on game strategy
    #board weightings borrowed from http://web.eecs.utk.edu/~zzhang61/docs/reports/2014.04%20-%20Searching%20Algorithms%20in%20Playing%20Othello.pdf
    def getMoveWeighted(self, game=None, moves=None, curr_weight=0, k=1, k_max=None):
        if game == None:
            game = self.game

        if moves == None:
            moves = game.valid_moves[game.piece[game.curr_player]]

        if k_max == None:
            k_max = k

        if k == 0:
            return curr_weight

        if game.curr_player == "White":
            best_weight = -1000
        if game.curr_player == "Black":
            best_weight = 1000
        
        
        if game.finished == False:
            for move in moves:
                w = curr_weight
                subgame = copy.deepcopy(game)
                
                subgame.playMove({"row": move[0], "col": move[1]}, subgame.curr_player, modify=True)
                #print(w)
                #print(move)
                #print(subgame.curr_player)
                if subgame.curr_player == "White":
                    w += self.weights[move[0]][move[1]]
                else: 
                    w -= self.weights[move[0]][move[1]]
                #print(w)
                
                subgame.findValidMoves("all")
                subgame.changePlayer()
                
                my_weight = self.getMoveWeighted(subgame, subgame.valid_moves[subgame.piece[subgame.curr_player]], w, k-1, k_max)
            
                if game.curr_player == "White":
                    if my_weight >= best_weight:
                        best_weight = my_weight
                        best_move = move
                if game.curr_player == "Black":
                    if my_weight <= best_weight:
                        best_weight = my_weight
                        best_move = move

        if k < k_max:
            #print("returning best weight: %d" % best_weight)
            return best_weight
        if k == k_max:
            #print("best weight found: %d" % best_weight)
            return {"row": best_move[0], "col": best_move[1]}
