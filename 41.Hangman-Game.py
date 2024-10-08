'''
Hangman Game Instructions:

Write a Python program to implement a Hangman game:

1. Choose a Word: Select a word for the player to guess.
2. Initialize Variables: Create a list for guessed letters and a counter for wrong guesses.

Game Loop:
1. Display the current state of the word.
2. Prompt the player to guess a letter.
3. Check if the letter is in the word:
4. If yes, reveal its positions.
5. If no, increase the wrong guess counter.

End Game:
1. Display a win message if the word is fully guessed.
2. Display a loss message if the wrong guesses exceed the limit.

'''













import random

list1 = ['Genesis', 'Mathew', 'Nahum', 'Proveb']

lives = 6


hangmanpic = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

chosen_word = random.choice(list1)

print(chosen_word)

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
        print(hangmanpic[lives])
        if lives == 0:
            game_over = True
            print(hangmanpic[lives])
            print('No guess chance remain, You lose.')
            
            
    if '_' not in display:
        game_over = True
        print('Congraturations, You win!')