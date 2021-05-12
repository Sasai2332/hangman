import random
from words import word_list

def play_hangman():
  x = random.choice(word_list)
  word = x.upper()
  word_completion = "_" * len(word)
  word_letters = set(word)
  guessed_letters = []
  guessed_words = []
  guessed = False
  tries = 6
  print("Let's play Hangman!")
  print(word_completion)
  print("\n")

  while not guessed and tries > 0 and len(word_letters) > 0:
      guess = input("guess a letter or word: ").upper()
      if len(guess) == 1 and guess.isalpha():
          if guess in guessed_letters:
              print("you already guessed this letter.")
              print("\n")
          elif guess not in word:
              print(guess + " is not in the word.")
              tries -= 1
              print("You have " + str(tries) + " tries/try left.")
              guessed_letters.append(guess)
              current_word = [letter if letter in guessed_letters else '_' for letter in word]
              print(" ", " ".join(current_word))
              print("guessed letters:" + str(guessed_letters))
              print("\n")
              if tries == 6:
                    print(
                      """
                        _____
                        |   | 
                        |   
                        |
                        |
                        |____""")
              elif tries == 5:
                  print(
                    """
                        _____
                        |   | 
                        |   O
                        |
                        |
                        |____""")
                  print("\n")
              elif tries == 4:
                  print(
                      """
                        _____
                        |   | 
                        |   O
                        |   | 
                        |
                        |____""")
                  print("\n")
              elif tries == 3:
                  print(
                      """
                        _____
                        |   | 
                        |   O
                        |  /|
                        |
                        |____""")
                  print("\n")
              elif tries == 2:
                  print(
                      """
                            _____
                            |   | 
                            |   O
                            |  /|/
                            |
                            |____""")
                  print("\n")
              elif tries == 1:
                  print(
                      """
                        _____
                        |   | 
                        |   O
                        |  /|/
                        |  /
                        |____""")
                  print("\n")
          else:
              print("good job!, " + guess + " is in the word")
              guessed_letters.append(guess)
              current_word = [letter if letter in guessed_letters else '_' for letter in word]
              print(" ", " ".join(current_word))
              print("guessed letters:" + str(guessed_letters))
              print("\n")
              if guess in word_letters:
                  word_letters.remove(guess)


      # when the guess is an entire word
      elif len(guess) > 1 and guess.isalpha():
          if guess in guessed_words:
              print("you already guessed the word " + guess)
          elif guess != word:
              print(guess + " is not the word")
              tries -= 1
              print("You have " + str(tries) + " tries left.")
              guessed_words.append(guess)
              print("\n")
              if tries == 6:
                  print(
                      """
                        _____
                        |   | 
                        |   
                        |
                        |
                        |____""")
              elif tries == 5:
                  print(
                      """
                          _____
                          |   | 
                          |   O
                          |
                          |
                          |____""")
                  print("\n")
              elif tries == 4:
                  print(
                      """
                        _____
                        |   | 
                        |   O
                        |   | 
                        |
                        |____""")
                  print("\n")
              elif tries == 3:
                  print(
                      """
                        _____
                        |   | 
                        |   O
                        |  /|
                        |
                        |____""")
                  print("\n")
              elif tries == 2:
                  print(
                      """
                            _____
                            |   | 
                            |   O
                            |  /|/
                            |
                            |____""")
                  print("\n")
              elif tries == 1:
                  print(
                      """
                        _____
                        |   | 
                        |   O
                        |  /|/
                        |  /
                        |____""")
                  print("\n")
          else:
              guessed = True
              guess == word

      else:
          print("not a valid guess :(")

# will exit while loop when player is out of tries or when the player has guess the word correctly

  if len(word_letters) == 0:
      print("congrats!")
  if tries == 0:
      print("sorry! you ran out of tries...")
      print("the word was " + word)
      print("""
                _____
                |   | 
                |   O
                |  /|/
                |  //
                |____""")
  if guessed == True:
      print("congrats! that is the full word.")

  print("\n")


  answer = input("would you like to play again? type 'y' or 'n': ").upper()

  print("\n")
  if answer == "Y":
      play_hangman()
  elif answer == "N":
      print("thanks for playing!")
  else:
      print("not a valid input!")


play_hangman()
