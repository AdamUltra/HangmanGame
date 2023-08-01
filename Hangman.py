import random
import time
turns = 15
start = True
guesses = ''
right_answer = 0
spaces = ["_", "_", "_", "_", "_", "_", "_", "_"]
library = ['laptop', 'pig', 'great', 'life', 'sun', 'computer', 'tower', 'cloak', 'cola']
print('let\'s play hangman!!')
word = str(random.choice(library))
guess = str(input('Input a character: '))
guess += guesses
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:
        print("\nYou Win")
        print("The word is: ", word)
        time.sleep(1000)
        break
    guess = str(input("guess a character:"))
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")
            print('The word is: ', word)
            time.sleep(1000)


