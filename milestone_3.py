while True:
    guess = input("guess one letter!")
    if len(guess) == 1:
        break 
    else:
        print("Invalid letter. Please, enter a single alphabectical character.")

