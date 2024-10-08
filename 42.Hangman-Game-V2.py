'''
Hangman game using external files

i.e hamngman stage, and hangman woords
'''

import random

import hangman_stage

import Hangman_words


lives = 6


chosen_word = random.choice(Hangman_words.books_of_bible)


# print(chosen_word)

display = []

game_over = False

for i in range(len(chosen_word)):
    display += '_'


while not game_over:
    guess_letter=input("Gues the letter: ")
    
    for position in range(len(chosen_word)):
        
        letter = chosen_word[position]        
        if letter == guess_letter:
            display[position] = guess_letter
            
    print(display)
    
    if guess_letter not in chosen_word:
        
        lives -= 1
        print(hangman_stage.stage[lives])
        
        print(f'you are remain with {lives} guess')
        
        if lives == 0:
            game_over = True
            print(hangman_stage.stage[lives])
            print('No guess chance remain, You lose.')
            
            
    if '_' not in display:
        game_over = True
        print('Congraturations, You win!')