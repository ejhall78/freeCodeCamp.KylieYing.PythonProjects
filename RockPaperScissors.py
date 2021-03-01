import random

def play():
    userans = input('Whats your choice? "r" for rock, "p" for paper, "s" for scissors \nTo end the game, enter "Quit" \n')
    computerans = random.choice(['r', 'p', 's'])

    if userans == 'Quit' :
        exit()

    if userans == computerans :
        return "\nIt's a tie!\n"

    if is_win(userans, computerans) == True :
        return '\nYou won!\n'

    return '\nYou lost!\n'

def is_win(player, opponent) :
    # r > s, s > p, p > r
    # return True if player wins

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
        return True

while True :
    print(play())