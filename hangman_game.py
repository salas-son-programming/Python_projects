# HANGMAN GAME

import random

my_words=("banane", "pomme", "pasteque", "ananas","orange")
my_dict={1:"o",
         2: (" o ",
             " | ",
             " "),
         3: (" o ",
            "/|",
             " ",),
         4: (" o ",
            "/|\\",
             " ",),
         5: (" o ",
             "/|\\",
             "/",),
         6: (" o ",
             "/|\\",
             "/ \\",)
         }
guess_word=random.choice(my_words)

def display_hint(guess_word):
    pass


def loose_checker(number_of_guess):
    for i in my_dict[number_of_guess]:
        print(i)

isRunning= True
hint = ["_"] * len(guess_word)
wrong_guess=0
while isRunning:
    display_hint(guess_word)

    print(" ".join(hint))
    guess = input("enter a letter: ").lower()
    if guess in guess_word:
        for i in range(len(guess_word)):
            if guess == guess_word[i]:
                hint[i]=guess
    elif guess not in guess_word:
        wrong_guess+=1
        if wrong_guess == 7:
            print("you have lost")
            isRunning = False
        elif wrong_guess<7:
            for i in my_dict[wrong_guess]:
                print(i)

    if "_" not in hint:
        print("won")
        isRunning = False


