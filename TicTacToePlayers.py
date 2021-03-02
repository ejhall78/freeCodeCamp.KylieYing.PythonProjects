import math
import random

class Player: 
    def __init__(self, letter) :
        # letter is 'x' or 'o'
        self.letter = letter

def get_move(self, game) :
    pass

class RandomComputerPlayer(Player):
    def __init__(self, letter) :
        super().__init__(letter)

    def get_move(self, game) :
    # gets a random valid spot for the next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter) :
        super().__init__(letter)

    def get_move(self, game) :
        valid_square = False
        val = None
        while not valid_square :
            square = input(self.letter + '\'s turn. Input move (0-8): ')

            # need to check that input is a number and is available on the board
            try :
                val = int(square)
                if val not in game.available_moves() :
                    raise ValueError
                valid_square = True
            except ValueError :
                print('Invalid square. Try again.')

        return val



