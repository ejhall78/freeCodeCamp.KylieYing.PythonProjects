import random
import string
from HangmanWords import words

def get_valid_word(words) :
    word = random.choice(words) # randomly chooses from words list
    while '-' in word or ' ' in word :
        word = random.choice(words) # chooses a different word until the word doesn't conatain - or space
    return word.upper()


def hangman() :
    word = get_valid_word(words) # get a valid word
    word_letters = set(word) # create a set containing the letters in the word
    alphabet = set(string.ascii_uppercase) # create a set containing all the possible letters capitalised
    used_letters = set() # create a set containing the letters already used

    # get input from user. If the letter inputted is not in the random word, add it to used letters
    # if the letter is in the random word remove the letter from the random word list
    
    lives = int(input('Choose your number of lives: '))
    
    while len(word_letters) > 0 and lives > 0 :
        # show user what letters they have used
        print(f'You have {lives} lives left and have used the letters: ', ' '.join(used_letters), '\n')

        # show user formatted word with unguessed letters and guessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word :', ' '.join(word_list), '\n')

        inp_letter = input('Guess a letter: ').upper() 
        if inp_letter in alphabet - used_letters :
            used_letters.add(inp_letter)
            if inp_letter in word_letters :
                word_letters.remove(inp_letter)

            else :
                lives -= 1
                print(f'Uh-oh! Letter not in word. You now have {lives} lives left \n')

        # if letter been tried already, let user know
        elif inp_letter in used_letters :
            print('You have already tried this letter. Please try again. \n')

        # only allow letters not characters
        elif inp_letter in used_letters :
            print('Invalid character. Please try again. \n')
    
    if lives == 0 :
        print(f'Sorry you died. The word was {word}\n')
    else :
        print(f'\nCongratualtions! You guessed the word {word}!!\n')

hangman()




