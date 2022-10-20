# THIS IS THE HANGMAN GAME
import random

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
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
 /|   |
      |
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
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()

# Randomly choose a word from the word_list and assign it to a variable called chosen_word
random_word = word_list[random.randint(0, len(word_list) - 1)]
print(random_word)

# For each letter in the random_word, add a "_" to 'display'
display = []
for _ in random_word:
    display.append('_')
print(display)
# Create a system of HP
print(hangman[0])
HP = 6
# Let the user guess again.
end_of_game = False
while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter!\n").lower()

    if guess in display: # do not let the user choose the same letter again
        print('You already guessed that one! Try a choosing a new letter!')
    else:

        # loop through each position in the random_word. If the letter at that position matches 'guess' then reveal it
        counter = 0
        correct_counter = 0
        guess_correctly = False
        for letter in random_word:
            counter += 1
            if guess == letter:
                display[counter - 1] = guess
                guess_correctly = True
                correct_counter += 1
        # Lose a life if guessed incorrectly, notify if guessed correctly
        if not guess_correctly:
            HP -= 1
            print(hangman[6 - HP])
            print('Try again!')
        else:
            print(f'You guessed {correct_counter} letters correctly!')

        # print the display so far
        print(display)
        if '_' not in display:
            end_of_game = True
            print('You win!')
        if HP == 0:
            end_of_game = True
            print('You lose!')
