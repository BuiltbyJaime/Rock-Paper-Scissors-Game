import random
import time

options = ["rock", "paper", "scissors"]

input("Dare to play? ")

time.sleep(3)


#Included the code in a function so I could call it again if the player chooses to 

 # Added the ability for the player to choose to play again or not after initial choice 

def choosingAgain ():
        again = input ("Want to play again? (yes/no) ")
        if again.lower()== "yes":
            gamelogic()
        if again.lower()== "no":
            print ("Have a good day!")
            exit
        else:
            print("Please type Yes or No")
            choosingAgain()


def gamelogic():
    
    player_choice = str(input("What is your choice?: ")).lower()    
    if player_choice in options:
        print(f'You have chosen {player_choice}, good luck!')
        time.sleep(1)
    else: 
        print(f'{player_choice} is not a valid entry, try again !')
        gamelogic()
    
    time.sleep(1)
    print("Computer is thinking about choosing")
    time.sleep(2)  

    
    
    # Here is the game logic for the choices including a tie 
    computerChoice = random.choice(options)
    if player_choice == computerChoice:
        print("It is a tie !")
        choosingAgain()
    elif player_choice == "rock" and computerChoice == "paper":
        print (f"You have lost, Computer chose {computerChoice}")
        choosingAgain()
    elif player_choice == "rock" and computerChoice == "scissors":
        print(f"Congratulations you have won! Computer chose {computerChoice} ")
        choosingAgain()
    elif player_choice == "paper" and computerChoice == "rock":
        print (f"Congratulations you have won! Computer chose {computerChoice}")
        choosingAgain()
    elif player_choice == "paper" and computerChoice == "scissors":
        print(f"You have lost, Computer chose {computerChoice}")
        choosingAgain()
    elif player_choice == "scissors" and computerChoice == "paper":
        print (f"Congratulations you have won! Computer chose {computerChoice}")
        choosingAgain()
    elif player_choice == "scissors" and computerChoice == "rock":
        print(f"You have lost, Computer chose {computerChoice}")
        choosingAgain()

gamelogic()

