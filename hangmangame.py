#hangman game

import random

def hang_man():
  words = ["baby", "ice"]
  display = []
  lives = 3
  chose = random.choice(words).lower()
  
  #loop the x number to match the characters count for the hidden words
  for i in range(len(chose)):
    display += "_"
  
  #create a var for deciding game win or lose
  end_of_game = False
  while end_of_game == False:
    print(display)
    guess = input("Enter a letter: ").lower()
    
    #check if guess is matching with any letter in chose
    #check indexing of the letter is chose, if anything that match with entered letter, if match then replace in display with indexing to match the position
    
    if guess in chose:
      for index in range(len(chose)):
        if chose[index] == guess:
          display[index] = guess
    else:
      lives -= 1
  
    if "_" not in display:
      end_of_game = True
      print("You Won! ")
  
    elif lives == 0:
      end_of_game = True
      print("You Lose")


while True:
  hang_man()
  rerun = input("Do you want to rerun the game? yes or no ").lower()
  if rerun == "no":
    break
    
  
