from milestone_2 import word as wrd 


while True:
    guess = input("guess one letter!")
    if len(guess) == 1 & (guess in wrd):
        print("good guess mate")
        break 
    else:
        print("Invalid letter. Please, enter a single alphabectical character.")    

