import random

def guess(x) :
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number :
        guess = int(input(f'Enter a random number between 1 and {x}: '))
        if guess > random_number :
            print('Sorry guess again. Your guess was too high \n')
        elif guess < random_number :
            print('Sorry guess again. Your guess was too low \n')
    print(f'Congratulations! Your guess {guess} was correct')

guess(int(input('Enter a range: ')))