#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import choice

words = ["test","jump", "teeth", "backpack", "catfish", "gravity", "coffee"]
numWrong = 0
listedWord = [None]


# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord
   # Greet the user
   print("\nLet's play a game of hangperson!")
 # Randomly select a word from the list of words
   word = choice(words)
   # Make the randomly selected word into a list object
   listedWord = list(word)

   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
   currentState = ["_"] * len(listedWord)

   # Print the initial state of the game
   printHangperson(currentState)

   # Start the game! Loop until the user either wins or loses
   while currentState != listedWord and numWrong < 6:
      guess = userGuess()
      currentState = updateState(guess, currentState)
      printHangperson(currentState)
   if  currentState == listedWord and numWrong < 6:
       print("You won! No noose is good noose!")
   else:
        print("Awe. You've decided to take a swing on the gallows.")


   # Determine if the user won or lost, and then tell them accordingly


# This helpful function prompts the user for a guess,
# accepting only single letters.
# DO NOT CHANGE
#
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
   while len(guess) != 1:
        if guess == "":
            print("\nYou have to guess a letter.")
        elif guess == "exit":
            exit()
    # If the user inputs multiple letters at once
        else:
            print("\nYou can't guess more than one letter at a time.")
        guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")

    # If the user inputs a letter they've already used
        #elif guess in used:
            #print("You already tried that letter.")
   return guess


# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
   global numWrong

# First, determine if the letter guessed is in the word.
   # If it isn't, tell the user and update the numWrong var
   # If it is, congratulate them and update the state of the game.
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   numInWord = listedWord.count(guess)
   for index, char in enumerate(listedWord):
       if char == guess:
           currentState[index] = guess
   if guess not in listedWord:
       print("you suck")
       numWrong += 1
   else:
       print("You don't suck")
   return currentState


     #missed += 1
# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

# This line runs the program on import of the module
hangperson()
