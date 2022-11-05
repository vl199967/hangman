import random 

word_list = ['mango','custard apple','lychee','orange','banana']

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("enter a radnom single letter")

if len(guess) == 1:
    print("good guess!")
else: 
    print("Oops! That is not a valid input.")    