'''
Board layout:
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

 2 players should take turns
------------------------------

 EXPECTED OUTPUT:
 === Tic Tac Toe ===
Player 1 name (X): player1
Player 2 name (O): player2

 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 


 player1 (X), enter position (1-9): 2

 1 | X | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 


player2 (O), enter position (1-9): 1

 O | X | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 

...

'''


# make the board
class Board:
    WINNING_COMBOS = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6],             # diagonals
    ]

    # initializer method
    def __init__(self):
        self.cells = [str(i + 1) for i in range(9)]

    # display board
    def display(self):
        print()
        for row in range(3):
            start = row * 3
            print(f" {self.cells[start]} | {self.cells[start+1]} | {self.cells[start+2]} ")
            if row < 2:
                print("-----------")
        print()

    # mark position with X or O


    # winner


    # when the board is fully marked



# create the player
class Player:
    # initializer method: takes players name and their chosen symbol X or O
    pass

    # make a move: player picks the position on the board where they want to put their X or O



# run the game
class TicTacToe:
    # initializer method
    def __init__(self):
        print("\n=== Tic Tac Toe ===")
        name1 = input("Player 1 name (X): ").strip() or "Player 1"
        name2 = input("Player 2 name (O): ").strip() or "Player 2"

        self.players = [
            Player(name1, "X"),
            Player(name2, "O"),
        ]
        self.board = Board()
        self.current = 0  # index into self.players
        pass


    # play method


    # switch player turn


    # method to run the game




