from TicTacToePlayers import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe :
    def __init__(self) :
        self.board = [' ' for _ in range(9)] # single list of 9 potential positions as our board
        self.current_winner = None # tracks who the winner is

    def print_board(self) :
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)] :
            print('| ' + '| '.join(row) + ' |')

    @staticmethod
    def print_board_nums() :
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board :
            print('| ' + '| '.join(row) + ' |')

    def available_moves(self) :
        moves = []
        for (i, spot) in enumerate(self.board) : # enumerate creates a list with assigned values to each item
            # eg ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ' :
                moves.append(i)
        return moves
        # this can also be written as return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter) :
        # if move is valid, make move (assign letter to square)
        # then return True. return false if move invalid
        if self.board[square] == ' ' :
            self.board[square] = letter
            if self.winner(square, letter) :
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter) :
        # winner if 3 in a row - we have to check all of the possibilities
        
        # row check
        row_in = square // 3
        row = self.board[row_in*3 : (row_in +1)*3]
            # if each spot in the row is the same,
            # make winner True so that current winner is set to the current letter
            # as in the function above
        if all([spot == letter for spot in row]) :
            return True

        # column check
        col_ind = square % 3
        column = [self.board[col_ind + (i*3)] for i in range(3)]
        if all([spot == letter for spot in column]) :
            return True

        # diagonal check
        # diagonal spaces can only be 0,2 (first row), 4 (centre), 6,8 (bottom row)
        # check if even:
        if square % 2 == 0 :
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]) :
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6] ] # right to left
            if all([spot == letter for spot in diagonal2]) :
                return True
        
        # if all these checks fail, winner is false until a check passes
        return False


    def empty_squares(self) :
        return ' ' in self.board

    def empty_squares_num(self) :
        return len(self.available_moves())


def play(game, x_player, o_player, print_game = True) :
    # return the winners letter if there is one or return None if it's a tie 
    
    if print_game :
        game.print_board_nums()

    letter = 'X' #starting letter

    while game.empty_squares():
        if letter == 'O' :
            square = o_player.get_move(game)
        else :
            square = x_player.get_move(game)

        if game.make_move(square, letter) :
            if print_game :
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner :
                if print_game :
                    print(letter + ' wins!')
                return letter

            if letter == 'X' :
                letter = 'O'
            else :
                letter = 'X'
            # can also be written as letter = 'O' if letter == 'X' else 'X'

            # leave a small gap between user input and computer output
            # this simulates the computer's 'thinking time'

        time.sleep(0.8)

    if print_game :
        print('It\'s a tie!')

if __name__ == '__main__' :
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)
