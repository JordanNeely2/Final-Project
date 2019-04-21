import reversi as rv
import copy

levels = 2

class ReversiAI:


    def __init__(self, game, level):
        self.game = game
        self.level = level
        self.game2 = copy.deepcopy(game)

    def getMove(self, level):
        if level == 1:
            return self.getMoveRandom()

        if level == 2:
            return self.getMoveMaxScore()

        if level == 3:
            return self.getMoveMinMoves()

    #return a random valid move
    def getMoveRandom(self):
        
        
        return


    #returns move with highest score for white after k moves
    def getMoveMaxScore(self, k=1):

        subgames = {}

        for move in self.game.valid_moves[self.game.piece["White"]]:
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


        return


    def test(self):
        print("Hello world!")
        print(self.game.board)
        print(self.game.poss_moves)
        print(self.game.valid_moves[self.game.b_piece])
        print(self.game.valid_moves[self.game.w_piece])

    def test2(self):
        print("Hello world 2...")
        print(self.game2.board)
        print(self.game2.poss_moves)
        print(self.game2.valid_moves[self.game.b_piece])
        print(self.game2.valid_moves[self.game.w_piece])
