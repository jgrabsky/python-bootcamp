import random

word_list = ["aardvark","baboon","camel"]

stages = [
    """
     _______
    |/      
    |      
    |      
    |      
    |      
    |
    =========""",
    """
     _______
    |/      |
    |      
    |      
    |      
    |      
    |
    =========""",
    """
     _______
    |/      |
    |      (_)
    |      
    |      
    |      
    |
    =========""",
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |
    =========""",
    """
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |      
    |
    =========""",
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      
    |
    =========""",
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / 
    |
    =========""",
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
    ========="""
]
lives = len(stages)
#print(lives)

chosen_word = random.choice(word_list)
#print(chosen_word)

print("_" * len(chosen_word))
correct_letters = []

game_over = False
while not game_over:

    guess = input("Guess a letter: ").lower()
    print(guess)

    display = ""
    guess_correct = False
    for letter in chosen_word:
        if letter == guess:
            guess_correct = True
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if not guess_correct:
        print(stages[-lives])
        lives -= 1
    print(display)

    if "_" not in display:
        game_over = True
        print("You won!")
    if lives <= 0:
        game_over = True
        print("You lost!")
    