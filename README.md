# Final-Project
User Manual for CS302 Reversi Final Project Alex Seagle, Charles Baker, Jordan Neely.
//Tested on Hydra Lab machines



--------Compiling Instructions

	To compile the programs on a Hydra machine, use

//For the game window program called Foo-Rendering.cpp, use
g++ Foo-Rendering.cpp -lSDL2 -lSDL2_image -o Game_Window

//For the game programs, they are written in Python 3. It it written with the intention of being compatible with Python 2, though that may not be the case. In particular, there might be problems with printing if using python 2. 

//Game_Window requires the Pieces2.xcf file.



--------Running Instructions

	To run the programs, start two terminals. In one terminal:

//To start the game with an algorithm that picks random moves, use	
./play_reversi --ai=1 --no-vis

//To start the game with an algorithm that tries to minimize the opposing player's moveset, use
./play_reversi --ai=2 --no-vis

//To start the game with an algorithm that tries to maximize its score in each round, use
./play_reversi --ai=3 --no-vis

//To start the game with an algorithm that tries to rate possible moves and choose the best, use
./play_reversi --ai=4 --no-vis

//For an improved version of the level 4 ai that looks deeper than one move, use
./play_reversi --ai=5 --no-vis

//To play with two humans, leave off --ai=x

//To play in the terminal, leave off --no-vis

	In the other terminal:

//To open the game window, use
./Game_Window



--------Game Instructions
	To play the game, the goal is to have the most pieces on the board. The player always uses the black pieces. One piece may be placed on the board per round if legal moves still exist. A move is legal if
the spaces between it and one or more friendly pieces vertically, horizontally, or diagonally are filled with enemy pieces. The enemy pieces between are then flipped to become friendly. If the move is 
legal for multiple strings of enemy pieces, then all of them may be flipped with the same move.

	Looking at the game window, the board is an 8 by 8 grid of tiles. A green tile is an empty space, a tile with a black circle is a black piece, a tile with a white circle is a white piece, and
a tile with a blue square is a legal move. To choose a move, click on the corresponding tile.

	The game ends when the current round has no possible moves. This can happen when the grid is full or when one or both sides have no more legal moves. The score will then be printed to the 
AI-selecting terminal.



--------Bugs
	One unreplicated bug crashed the game. Game seemed to read input incorrectly? Unclear what caused this bug or how to replicate.
	There are minor lines through a few letters in the game window that do not show in the original image file.
	AI level 5 had a bug that sometimes crashed the game very close to the end when it tried to look too deep past the end of the game. It *should* be fixed, though it's possible it's still lingering.
