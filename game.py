import random
import time

options = ["rock", "paper", "scissors"]

input("Dare to play? ")

time.sleep(2)

print("Haha, You have no control here!!")

time.sleep(2)


player_choice = str(input("What is your choice?: ")).lower()

if player_choice in options:
    print(f'You have chosen {player_choice}, good luck!')
else:
    print(f'{player_choice} is not a valid entry, try again !')
  


computerChoice = random.choice(options)
