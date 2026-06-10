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
player_guess = input("Guess a letter: ")
if len(player_guess) != 1 and not player_guess.isalpha():
    print("E3")
elif len(player_guess) != 1:
    print("E1")
elif not player_guess.isalpha():
    print("E2")
else:
    print(player_guess.lower())

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