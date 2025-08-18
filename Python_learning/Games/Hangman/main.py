import random
# import words
from words import word_list

logo = [''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
''']
hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
random_word = random.choice(word_list)
# print(random_word)
lives = 6

guess = ["_"] * len(random_word)

print(f"{logo[0]}")
while not end_of_game:
    guess_letter = input("Enter a letter to Guess a Word:  ").lower()
    for i in range(0, len(random_word)):
        if guess_letter == random_word[i]:
            guess[i] = random_word[i]

    print(f"{guess}")

    if guess_letter not in random_word:
        lives -= 1
        print(f"{hangman[lives]}")
        if lives == 0:
            end_of_game = True
            print("You Lose !")
            print(f"Actual word to guess was {random_word}")

    my_lst_str = ''.join(map(str, guess))
    if "_" not in my_lst_str:
        print("You Won !")
        end_of_game = True


