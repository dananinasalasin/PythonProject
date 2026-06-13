def check_valid_input(letter_guessed, old_letters_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    result = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

HANGMAN_ASCII_ART = """Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/"""

MAX_TRIES = 6

HANGMAN_PHOTOS = {
    0: """
x-------x
""",
    1: """
x-------x
|
|
|
|
|
""",
    2: """
x-------x
|       |
|       0
|
|
|
""",
    3: """
x-------x
|       |
|       0
|       |
|
|
""",
    4: """
x-------x
|       |
|       0
|      /|\\
|
|
""",
    5: """
x-------x
|       |
|       0
|      /|\\
|      /
|
""",
    6: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""
}
print(HANGMAN_ASCII_ART)
print(MAX_TRIES)

player_string = input("Please enter a word: ")
result = " ".join("_" * len(player_string))
print(result)

old_letters = ['a', 'b', 'c']
print(show_hidden_word(player_string, old_letters))
player_guess = input("Guess a letter: ")

if try_update_letter_guessed(player_guess, old_letters):
    print(True)
else:
    print(False)

print_hangman(3)