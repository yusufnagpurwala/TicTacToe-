import math
import time
import sys
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_move(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid retirn false
        if self.board[square] == ' ':
            self.board[square] = letter 
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True
        # check column
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in col):
            return True
        
        # check diagonals
        # but only if sqauare is an even number (0,2,4,6,8) these are the only possibility
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # lef to right diagonal
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True
            
        # if all these test fails
        return False

def play(game, x_player, o_player, print_game=True):
    def play_game():
        if print_game:
            game.print_board_nums()

        letter = 'X' # starting letter
        # iterate while the game still has empty squares
        while game.empty_squares():
            # get move from the appropriate player
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)

            if game.make_move(square, letter):
                if print_game:
                    print(f'{letter} makes a move to square {square}')
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter
                # after a move is made we have to alternate letter
                letter = 'O' if letter == 'X' else 'X' # switches player
            
            time.sleep(1) 
        
        if print_game:
            print('Its a Tie!')
        print("\nPlay Again?\n")
        while True:
            playagain = input("Enter Y to continue or Q to Quit\n\n")
            if playagain.lower() not in ['y', 'q']:
                continue
            else:
                break
        if playagain.lower() == 'y':
            return play_game(game, x_player, o_player, print_game=True)
        else:
            print("Thanks for Playing!!")
            sys.exit("See you soon...Bye 👋👋")
    return play_game


if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play_TicTacToe = play(t, x_player, o_player, print_game=True)
    play_TicTacToe()