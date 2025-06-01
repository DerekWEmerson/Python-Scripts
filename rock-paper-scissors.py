# Add a tally system and allow the game to loop. Create an exit function.

import random

def main():
  pl_choice = playerchoice()
  print(f"{pl_choice}")
  com_choice = computerchoice()
  print(f"{com_choice}")
  contest(pl_choice, com_choice)

def playerchoice():
  while True:
    pl_choice = input(
    f"Welcome to Rock Paper Scissors!\n"
    f"1. Rock\n"
    f"2. Paper\n"
    f"3. Scissors\n"
    "\n"
    f"Please choose an option: "
    )
    if pl_choice == "1":
      pl_choice = "rock"
      return pl_choice
    elif pl_choice == "2":
      pl_choice = "paper"
      return pl_choice
    elif pl_choice == "3":
      pl_choice = "scissors"
      return pl_choice
    else:
      print("Please type 1, 2, or 3.")

def computerchoice():
  options = ["rock", "paper", "scissors"]
  com_choice = random.choice(options)
  return com_choice

def contest(pl_choice, com_choice):
  winning_outcomes = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
  if pl_choice == com_choice:
    print("It's a tie!")
  elif (pl_choice, com_choice) in winning_outcomes.items():
    print(f"You win against {com_choice}!")
  else:
    print(f"You lost against {com_choice}.")
  
main()