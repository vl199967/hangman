from milestone_2 import word as wrd 

'''
while True:
    guess = input("guess one letter!")
    if len(guess) == 1 & (guess in wrd):
        print("Good guess! {} is in the word.".format(guess))
        break 
    else:
        print("Not singular character input or guessed letter is not in the word. Try again.")    
'''
def check_guess():
    while True:
        guess = input("guess one letter!")
        if len(guess) == 1 & (guess in wrd):
            print("Good guess! {} is in the word.".format(guess))
            break 
        else:
            print("Not singular character input or guessed letter is not in the word. Try again.")   

check_guess() 