import reversi as rv
import copy
import random
import time

levels = 4

class ReversiAI:


    def __init__(self, game, level):
        self.game = game
        self.level = level

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
    def getMoveWeighted(self, k=1):

        with open('board_weight.txt', 'r') as f:
            weights = []

            for line in f:
                L = []
                for weight in line.split():
                    L.append(int(weight))

                weights.append(L)
        
        best_weight = -50

        for move in self.game.valid_moves[self.game.piece["White"]]:
            if weights[move[0]][move[1]] > best_weight:
                best_weight = weights[move[0]][move[1]]
                best_move = move

        return {"row": best_move[0], "col": best_move[1]}
