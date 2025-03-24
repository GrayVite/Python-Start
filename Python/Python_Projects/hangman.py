import random
from wordslist import words

# dictionary of key:tuple
# Each tuple has three items, each item has three characters
hangman_art = {0: ("   ", "   ", "   "), 
               1: (" o ", "   ", "   "), 
               2: (" o ", " | ", "   "), 
               3: (" o ", "/| ", "   "), 
               4: (" o ", "/|\\", "   "),  # use double back slash to display one back slash
               5: (" o ", "/|\\", "/  "), 
               6: (" o ", "/|\\", "/ \\")} 

#for line in hangman_art[5]: # In the first tuple(zero index), we print each item of tuple in a new line
#    print(line)

def display_man(wrong_guesses):
    print("***********************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***********************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words) # return a list 
    hint = ["_"] * len(answer) # multiplies the number of elements by that number of times

    wrong_guesses = 0

    guessed_letters = set() # in python, to create an empty set, call the set() function

    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        # Checks if there is only one letter or if the letter is not an alphabet
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
        
        # check to see if we have already guessed the letter
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        # If we haven't guessed the letter, add it to the set of guessed_letters
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)): # The for loop checks which index matches, and replaces the underscore in hint at index
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Your WIN")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You LOSE")
            is_running = False



if __name__ == '__main__':
    main()