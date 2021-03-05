import random

def computer_guess(x) :
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = low # could be low or high as they are the same
        feedback = (input(f'Is {guess} too high (H), too low (L), or correct (C) \n')).lower()
        if feedback == 'h' :
            high = guess -1
        elif feedback == 'l' :
            low = guess +1
    print(f'Yay! Computer guessed your number, {guess}, correctly!')

computer_guess(int(input('Enter a range: ')))