"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
  """Psuedo-code Hints
  
  When the program starts, we want to:
  ------------------------------------
  1. Display an intro/welcome message to the player.
  2. Store a random number as the answer/solution.
  3. Continuously prompt the player for a guess.
    a. If the guess greater than the solution, display to the player "It's lower".
    b. If the guess is less than the solution, display to the player "It's higher".
  
  4. Once the guess is correct, stop looping, inform the user they "Got it"
        and show how many attempts it took them to get the correct number.
  5. Let the player know the game is ending, or something that indicates the game is over.
  
  ( You can add more features/enhancements if you'd like to. )
  """
  # write your code inside this function.
  #

  # Generate title
  TITLE = "Number guessing game by Sccroix"
  print("-" * len(TITLE))
  print(TITLE)
  print("-" * len(TITLE))

  highscore = 0

  #Start a Round of Guessing
  def play_round():
    num_guesses = 0

    #Generate a random number between 1 - 10
    rand_num = random.randint(1,10)
    print("The random number is {}".format(rand_num))

    while True:
      guess = input("Guess a number between 1 and 10: ")

      try:
        guess = int(guess)
      except:
        print("That was not a number")
        continue
      
      num_guesses += 1

      print("this is guess number {}".format(num_guesses))
      if guess == rand_num:
        print("Correct")
        break
      else:
        print("That was wrong. Try again")
        continue



    #Ask player to guess Number

    #Compare Number to actual
      
      # If Greater say so

      # If Lower say so

      # If correct respond with number of trys



  #This is the main loop of the game
  play_round()


# Kick off the program by calling the start_game function.
start_game()