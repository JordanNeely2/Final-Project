import reversi as rv
import copy

levels = 3

class ReversiAI:


    def __init__(self, game, level):
        self.game = game
        self.level = level

    def getMove(self, level):
        if level == 1:
            return self.getMoveRandom()

        if level == 2:
            return self.getMoveMaxScore()

        if level == 3:
            return self.getMoveMinMoves()

        if level == 4:
            return self.getMoveMaxSMinM()

        if level == 5:
            return self.getMoveMaxScore(k=2)

    #return a random valid move
    def getMoveRandom(self):
        
        
        return


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


    #maximize score, if two moves are tied, tiebreak with min opp. moves
    def getMoveMaxSMinM(self, k=1):


        return {"row": best_move[0], "col": best_move[1]}
