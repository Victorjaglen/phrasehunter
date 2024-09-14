from .phrase import Phrase
import random


class Game:

    def __init__(self):
        # Initialize game variables
        self.missed = 0
        self.phrases = ['Camelot is a silly place',
                        'He is all hat and no cattle',
                        'Tis but a scratch',
                        'I shall not repeat myself',
                        'Go Berserk']
        self.active_phrase = None
        self.guesses = []
        self.lives = 5

    def get_random_phrase(self):
        # Pick a random phrase and create a Phrase object
        phrase_text = random.choice(self.phrases)
        self.active_phrase = Phrase(phrase_text)
        return self.active_phrase

    def welcome(self):
        # Display a welcome message
        print('\n---Welcome to the Phrase Hunter---')
        print(f"\nTry to guess the phrase!")

    def get_guess(self):
        # Display the current state of the phrase
        print(self.active_phrase.display())

        while True:
            guess = input('\nGuess a letter: ')

            # Check if the guess has already been made
            if guess in self.guesses:
                print(f"\nYou've already guessed '{guess}'. Try a different letter.\n")
                print(self.active_phrase.display())
                continue

            # Check for valid input
            if len(guess) != 1 or not guess.isalpha():
                print('\nInvalid input! Please guess only a single alphabet letter (no numbers or special characters).\n')
                print(self.active_phrase.display())
                continue

            break


        # Update lives and guessed letters based on the guess
        if guess.lower() not in self.active_phrase.phrase:
            self.lives -= 1
            print(f'\nWrong Guess! You have {self.lives} out of {5} lives remaining!\n')
            self.missed += 1
        else:
            self.active_phrase.check_letter(guess)
            self.active_phrase.display()
            self.guesses.append(guess)


    def game_over(self):
        # Display the outcome of the game
        if self.missed > 4:
            print('You lose')
        elif self.active_phrase.check_complete():
            print(f'\n{self.active_phrase.display()}')
            print('\nCongrats!!! You Guessed it right!')
        else:
            print('\nKeep Trying')

    def play_again(self):
        while True:

            prompt = input('\nWould you like to play again (y/n): ')

            # Check for valid input
            if prompt.lower() not in ['y', 'n']:
                print("\nInvalid input! Please enter 'y' for Yes or 'n' for No.")
                continue

            if prompt.lower() == 'y':
                # Reset game state and start a new game
                self.missed = 0
                self.guesses = []
                self.lives = 5
                self.welcome()
                self.active_phrase = self.get_random_phrase()
                while self.missed <= 4 and not self.active_phrase.check_complete():
                    self.get_guess()
                self.game_over()
            else:
                # Exit the loop if the user does not want to play again
                print('\nHave a good day')
                break


    def start(self):
        # Start the game and handle replay logic
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        while self.missed <= 4 and not self.active_phrase.check_complete():
            self.get_guess()
        self.game_over()
        self.play_again()
