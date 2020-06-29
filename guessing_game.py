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
        print("Please enter your number as an integer (1-10)")
        continue
      
      num_guesses += 1

      if guess == rand_num:
        print("You got the answer correct on guess number {}".format(num_guesses))
        break
      elif guess > rand_num:
        print("Guess number {}: That was too High".format(num_guesses))
        continue
      elif guess < rand_num:
        print("Guess number {}: That was too Low".format(num_guesses))
        continue

    return num_guesses






  # This is the main loop of the game
  # Generate title
  title = "Number guessing game by Sccroix"
  print("-" * len(title))
  print(title)
  print("-" * len(title))

  highscore = 0

  while True:
    score = play_round()

    if highscore == 0:
      highscore = score
      print("you just set the highscore at {} guesses".format(highscore))
    elif score < highscore:
      highscore = score
      print("you just set the highscore at {} guesses".format(highscore))
    else:
      print("you didn't beat the high score")
    
    continue_playing = input("Do you want to continue playing (y/n): ")
    if continue_playing == "y":
      continue
    elif continue_playing == "n":
      break




  print("The final highscore was {}".format(highscore))


# Kick off the program by calling the start_game function.
start_game()