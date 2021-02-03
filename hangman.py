import random

word_list = ["detail", "gorgeous", "gentle", "soft", "glass", "shrill", "stare", "deserted", "strip", "defeated", "black and white", "remember"]

x = random.choice(word_list)
word = x.upper()
word_completion = "_" * len(word)
guessed = False
guessed_letters = []
guessed_words = []
tries = 6
print("Let's play Hangman!")
print(word_completion)
print("\n")
while not guessed and tries > 0:
  guess = input("please guess a letter or word: ").upper()
  if len(guess) == 1 and guess.isalpha():
    if guess in guessed_letters:
                print("you already guessed this letter.")
    elif guess not in word:
                print(guess + " is not in the word.")
                tries -= 1
                print("You have " + str(tries) + " tries left.")
                guessed_letters.append(guess)
    else:
      print("good job!, " + guess + " is in the word")
      guessed_letters.append(guess)
      word_as_list = list(word_completion)
      indices = [i for i, letter in enumerate(word) if letter == guess]
      for index in indices:
        word_as_list[index] = guess
      word_completion = "".join(word_as_list)
      if "_" not in word_completion:
        guessed = True
  elif len(guess) == len(word) and guess.isalpha():
    if guess in guessed_words:
      print("you already guesseed the word " + guess)
    elif guess != word:
      print (guess + " is not in the word")
      tries -= 1
      print("You have " + str(tries) + " tries left.")
      guessed_words.append(guess)
    else:
      guessed = True
      word_completion = word
  else:
    print("not a valid guess :(")
  print(word_completion)
  print("\n")
