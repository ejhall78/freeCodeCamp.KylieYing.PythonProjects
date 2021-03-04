import random
import re


# we can create an object to represent the board/game
# this is so that we can create functions that we can apply to each game board (object)

class Board:
    def __init__(self, dim_size, num_bombs):
        # we can keep track of these parameters for later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # initialize a board
        # we can do this with a helper function that we made
        # we can also make this function plant the bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()


        # initialize a set to keep track of places that have already been dug
        # we can save tuples of (row, col) into this set
        self.dug = set() # if we were to dig at 0, 0 then self.dug -> {(0,0)}

    def assign_values_to_board(self):
        # now that the bombs are planted, we can assign each square a value which tells the user 
        # how many bombs are next to that square. These values can only range from 0-8
        # if we pre-compute these, it will save us from having to check around the board later on
        
        # if our square is a bomb, leave this square alone
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # we need to iterate through each of the neighboring positions
        # and add up the number of bombs as we go
        # eg top left: (row -1, col -1)
        # top middle: (row -1, col) and so on...

        # we need to make sure we don't go out of bounds, eg if we check a square on the edge of the board
        # in order to make sure we don't go out of bounds, we can use a min() and max() limiter in our ranges
        # we would take the max out of 0 and row -1, and the min out of dim size -1 and row +1 
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) +1):
            for c in range(max(0, col -1), min(self.dim_size -1, col + 1) +1):
                if r == row and c == col: # this is our original position that we're checking
                    continue
                if self.board[r][c] == '*': # if our checked postion is a bomb, add 1 to total neighboring bombs
                    num_neighboring_bombs += 1
        
        return num_neighboring_bombs

    def make_new_board(self):
        # construct a board based on dim size and num bombs
        # as we are making a 2D board, a list of lists would be an appropriate structure

        # generate new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array containing a list for each row
        # like this:
        # [[None, None, .... None],
        #  [None, None, .... None],
        #  [....                 ],
        #  [None, None, .... None]]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            # returns a random integer between the higher and lower limits of the board
            loc = random.randint(0, self.dim_size**2-1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            # we will represent a bomb as '*'
            # if there is a bomb already on a square, we should keep going
            if board[row][col] == '*':
                continue
            
            board[row][col] = '*' # plant the bomb
            bombs_planted += 1 # count bombs planted to make sure we stop at specified num bombs

        return board

    def dig(self, row, col):
        # dig at user specified location
        # retrun True if successful dig, False if bomb and therefore GAMEOVER!

        # the scenarios:
        # 1. dig at bomb location -> GAMEOVER!
        # 2. dig at location with neigboring bombs -> finish dig
        # 3. dig at location with no neighboring bombs -> recursively dig until we find a bomb/s

        # keep track of dug locations by adding a tuple to our set() we initialised with
        self.dug.add((row, col))

        # scenario 1
        if self.board[row][col] == '*':
            return False
        # scenario 2
        elif self.board[row][col] > 0:
            return True
        
        # scenario 3
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) +1):
            for c in range(max(0, col -1), min(self.dim_size -1, col + 1) +1):
                if (r, c) in self.dug: #don't dig alreadt dug locations
                    continue
                self.dig(r, c)

        # 
        return True

    def __str__(self):
        # this is a dunder function that prints out what this fucntion returns whenever you 
        # call print on this object
        # return a string that shows the board to the player

        # create an array that represents what the user will see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # now put this in a string
        # the following formatting code was copied from:
        # https://github.com/kying18/minesweeper/blob/main/minesweeper.py
        
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
 

def play(dim_size = 10, num_bombs = 10):
    # 1. create board and plant bombs

    board = Board(dim_size, num_bombs)
    # 2. show the user the board ask user where they want to dig


    # 3. a) if dig location is a bomb, show game over message
    #    b) if dig location is not a bomb, dig recursively until each square is at least
    #  to a bomb
    # 4. repeat steps 2 and 3a/b until there are no more places to dig ie VICTORY!
    safe = True
    
    while len(board.dug) < board.dim_size**2 - num_bombs:
        print(board)
        
        # check if input is valid
        
        is_valid = False

        while is_valid == False:
            try:
                user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
                row, col = int(user_input[0]), int(user_input[-1])
                is_valid = True
            except:
                print('\nInvalid position. Please enter a valid postion as row,col\n')
                continue     
       
       # check if input is out of bounds
        if row < 0 or row >= board.dim_size or col < 0 or col > board.dim_size:
            print('\nInvalid position. Please try again\n')
            continue

        # if input is valid, we can dig there
        safe = board.dig(row, col)
        if not safe:
            # means they hit a bomb!!
            break
        
    # if the user has dug all the square and not hit any bombs, they win!
    if safe:
        print('\nCONGRATULATIONS!!! YOU CLEARED ALL THE MINES!')
    else:
        print('\nBOOM!!! SORRY GAME OVER...')
        # reveal the uncovered board
        # take every single combination of r, c and put in dug
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)] 
        print(board)

if __name__ == '__main__': # good practice - only runs the code in this file if running this file
    play()