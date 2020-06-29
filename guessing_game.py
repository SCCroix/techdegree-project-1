"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

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


import random

def play_round():
  #This will play a round and return a score
  score = 0

  #Generate a random number between 1 - 10
  rand_num = random.randint(1,10)
  
  #Loop through guesses until one is right
  while True:
    # Get a valid input from the user
    try:
      guess = input("Guess a number between 1 and 10: ")
      guess = int(guess)
    except ValueError:
      print("Thats not an integer")
      continue

    if guess > 10:
      print("That integer is too large")
      continue
    elif guess < 1:
      print("That integer is too small")
      continue
    
    # Increase score (guess count) after a valid input
    score += 1
    
    # Compare the input to random number
    if guess == rand_num:
      print("\nCorrect! its {}".format(rand_num))
      print("You got the answer correct on guess number {}".format(score))
      break
    elif guess > rand_num:
      print("Guess {}: It's Lower".format(score))
      continue
    elif guess < rand_num:
      print("Guess {}: It's Higher".format(score))
      continue

  return score


def start_game():
  # Handle Title, Highscore, and if the player wants to play again

  #Generate Title
  title = "Number guessing game by Sccroix"
  print(title)
  print("-" * len(title))

  highscore = 0

  #Play rounds until the player opts out
  play = True
  while play == True:
    score = play_round()

    # Manage the Highscores
    if highscore == 0:
      highscore = score
      print("You just set the highscore at {} guesses".format(highscore))
    elif score < highscore:
      highscore = score
      print("You just set the highscore at {} guesses".format(highscore))
    else:
      print("You didn't beat the high score")
    

    # Prompt if player wants to play again 
    def play_again():
      play = input("Do you want to play again (y/n)")
      if play not in ["y", "n"]:
        raise ValueError("You must respond as a y or n")
      else:
        return play == "y"
    
    while True:
      try:
        play = play_again()
      except ValueError as err:
        print("Whoops try again")
        print("({})".format(err))
        continue
      break

  # End the game and say Good bye
  print("\nThank you for playing")
  print("The final highscore was {}".format(highscore))


# Kick off the program by calling the start_game function.
start_game()

