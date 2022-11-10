import milestone_4 as ms4 

worz = ['mango','pear','grape','orange','nectarine']

def play_game(word_list):
    game = ms4.Hangman(word_list,num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
        elif game.num_lives>0:
            game.ask_for_input()
        if not (game.num_lives==0 and game.num_letters>0):
            print("You won the game!")    

play_game(worz)      