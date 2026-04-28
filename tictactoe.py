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
    def mark(self, spot, value):
        if self.cells[spot-1] == 'O' or self.cells[spot-1] == 'X':
            raise ValueError("Spot is already taken")
        if value == True:
            self.cells[spot-1] = 'X'
        else:
            self.cells[spot-1] = 'O'

    # winner
    def check_winner(self):
        for i in range(len(self.WINNING_COMBOS)):
            combo = self.WINNING_COMBOS[i]
            
            if self.cells[combo[0]] == self.cells[combo[1]] == self.cells[combo[2]]:
                return self.cells[combo[0]]
                
        return None

    # when the board is fully marked
    def ful(self):
        for i in range(9):
            if self.cells[i] != 'X' and self.cells[i] != 'O':
                return False # Board is not full
        return True


# create the player
#John
class Player:
    # initializer method: takes players name and their chosen symbol X or O
    def __init__(self):


    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    # make a move: player picks the position on the board where they want to put their X or O
    def make_move (self,board):
        while True:
            boardselection = input(f'{self.name}({self.symbol}) Enter a spot a board that is Valid(1-9):'):
            if boardselection.isdigit():
                boardselection_Isdigit = int(boardselection)
                if 1 <= boardselection_Isdigit <= 9:
                    boardselection_Isdigit2 = int(boardselection_Isdigit)
                    #subract one as computer sees boards as 0-8
                    XOpositions_on_board = boardselection_Isdigit2 - 1
                    #check to see if there is no previous placement there 
                    if board.cells[XOpositions_on_board] not in ['X','O']:
                        return XOpositions_on_board
                    else:
                        print('Spot Taken, Please try again.')
                else:
                    print('Not a Valid Number from 1-9, Please try again.')
            else:
                print('Not a Number, Please try again.')
pass

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
    John


    # switch player turn
    Jack


    # method to run the game
    Jack




