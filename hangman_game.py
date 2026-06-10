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
player_guess = input("Guess a letter: ")
print(player_guess)

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