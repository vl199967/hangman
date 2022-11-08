
import milestone_3 as ms3
import random

class Hangman():
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list #the word list, passed in as a param, from which a word is randomly drawn to be guessed by the player
        self.num_lives = num_lives #the number of tries a player has before the hangman is complete, set to five by default
        self.word = random.choice(word_list) # the word randomly drawn from the word list
        self.word_guessed = ['_'] * len(self.word) # a list of letters of the word, with _ for each letter not yet guessed.
        self.num_letters =  len(list(set(self.word))) # number of unique letters in the word. set() does not allow repeating elements, list() creates list, len() calculates the num of elements
        self.list_of_guesses = [] # number of tried guesses, initially empty. 

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! {} is in the word.".format(guess))

    def ask_for_input(self):
        while True:
            guess = input("guess one letter!")
            if not (guess.isalpha() and len(guess)==1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("you already tried that letter!")
            else:
                self.check_guess(self,guess)
                self.list_of_guesses.append(guess)        







        