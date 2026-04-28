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

    def __init__(self):
        self.cells = [str(i + 1) for i in range(9)]

    def display(self):
        print()
        for row in range(3):
            start = row * 3
            print(f" {self.cells[start]} | {self.cells[start+1]} | {self.cells[start+2]} ")
            if row < 2:
                print("-----------")
        print()

    def mark(self, spot, value):
        # Your logic: spot is 1-9, so we subtract 1 for the list index
        if self.cells[spot-1] == 'O' or self.cells[spot-1] == 'X':
            raise ValueError("Spot is already taken")
        if value == True:
            self.cells[spot-1] = 'X'
        else:
            self.cells[spot-1] = 'O'

    def check_winner(self):
        for combo in self.WINNING_COMBOS:
            if self.cells[combo[0]] == self.cells[combo[1]] == self.cells[combo[2]]:
                return self.cells[combo[0]]
        return None

    def ful(self):
        for i in range(9):
            if self.cells[i] != 'X' and self.cells[i] != 'O':
                return False 
        return True


# create the player
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # Keeping your specific input validation logic
    def make_move(self, board):
        while True:
            boardselection = input(f'{self.name} ({self.symbol}), enter position (1-9): ')
            if boardselection.isdigit():
                boardselection_Isdigit = int(boardselection)
                if 1 <= boardselection_Isdigit <= 9:
                    # check to see if there is no previous placement there 
                    # (Note: we check boardselection_Isdigit - 1 to match list indexing)
                    if board.cells[boardselection_Isdigit - 1] not in ['X','O']:
                        return boardselection_Isdigit 
                    else:
                        print('Spot Taken, Please try again.')
                else:
                    print('Not a Valid Number from 1-9, Please try again.')
            else:
                print('Not a Number, Please try again.')


# run the game
class TicTacToe:
    def __init__(self):
        print("\n=== Tic Tac Toe ===")
        name1 = input("Player 1 name (X): ").strip() or "Player 1"
        name2 = input("Player 2 name (O): ").strip() or "Player 2"

        self.players = [
            Player(name1, "X"),
            Player(name2, "O"),
        ]
        self.board = Board()
        self.current = 0 

    def switch_turn(self):
        self.current = 1 - self.current

    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current]
            
            is_x = (self.current == 0)
                
            spot = current_player.make_move(self.board)
            
            self.board.mark(spot, is_x)
            
            winner = self.board.check_winner()
            if winner != None:
                self.board.display()
                print(f"Congratulations! {current_player.name} ({winner}) wins!")
                break 
                
            if self.board.ful() == True:
                self.board.display()
                print("The board is full! It's a tie!")
                break 
                
            self.switch_turn()

# Execution
if __name__ == "__main__":
    game = TicTacToe()
    game.play()