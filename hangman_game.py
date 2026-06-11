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

print(HANGMAN_ASCII_ART)
print(MAX_TRIES)

player_string = input("Please enter a word: ")
result = " ".join("_" * len(player_string))
print(result)

old_letters = ['a', 'b', 'c']
player_guess = input("Guess a letter: ")

if try_update_letter_guessed(player_guess, old_letters):
    print(True)
else:
    print(False)

print("""
picture 1:
    x-------x
""")

print("""
picture 2:
    x-------x
    |
    |
    |
    |
    |
""")

print("""
picture 3:
    x-------x
    |       |
    |       0
    |
    |
    |
""")

print("""
picture 4:
    x-------x
    |       |
    |       0
    |       |
    |
    |
""")

print("""
picture 5:
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""")

print("""
picture 6:
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""")

print("""
picture 7:
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
""")