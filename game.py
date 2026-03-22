import random
import time # Added this so there are delays between code

options = ["rock", "paper", "scissors"]

computerCelebrations = ["Computer just emoted on you", "Computer just flipped the table and laughed in your face", "Computer just posted their win on social media"]


def start():
    dare = input("Ready to play now ? ")
    if dare.lower()== "yes":
        print("Yay!")
        time.sleep(1)
        print("One sec! ...  Computer is warming up their hands")
        time.sleep(3)
        gamelogic()
    elif dare.lower()== "no":
            print ("....wimp!")
            time.sleep(4)
            start()
    else:
            print("Please type Yes or No start")
            start()

time.sleep(3)


#Included the code in a function so I could call it again if the player chooses to 

# Added the ability for the player to choose to play again or not after initial choice 

def choosingAgain ():
        again = input ("Want to play again? (yes/no) ")
        if again.lower()== "yes":
            gamelogic()
        elif again.lower()== "no":
            print ("Have a good day!")
        else:
            print("Please type Yes or No to choosing again")
        


def gamelogic():
    
    playerChoice = str(input("What is your choice?: ")).lower()    
    if playerChoice in options:
        print(f'You have chosen {playerChoice}, good luck!')
        time.sleep(2)
        print("Computer is selecting their choice")
        time.sleep(3) 
        print("Sorry....the computer is visibily nervous")
        time.sleep(4)
        
    else: 
        print(f'{playerChoice} is not a valid entry, try again !')
        time.sleep(1)
        gamelogic()
    
    
    
    
    # Here is the game logic for the choices including a tie. 
    
    computerChoice = random.choice(options) 
    if playerChoice == computerChoice:
        print("It is a tie !")
        choosingAgain()
    elif playerChoice == "rock" and computerChoice == "paper":
        print (f"You have lost, Computer chose {computerChoice}")
        time.sleep(2)
        print (random.choice(computerCelebrations))
        choosingAgain()
    elif playerChoice == "rock" and computerChoice == "scissors":
        print(f"Congratulations you have won! Computer chose {computerChoice} ")
        choosingAgain()
    elif playerChoice == "paper" and computerChoice == "rock":
        print (f"Congratulations you have won! Computer chose {computerChoice}")
        choosingAgain()
    elif playerChoice == "paper" and computerChoice == "scissors":
        print(f"You have lost, Computer chose {computerChoice}")
        time.sleep(2)
        print (random.choice(computerCelebrations))
        choosingAgain()
    elif playerChoice == "scissors" and computerChoice == "paper":
        print (f"Congratulations you have won! Computer chose {computerChoice}")
        choosingAgain()
    elif playerChoice == "scissors" and computerChoice == "rock":
        print(f"You have lost, Computer chose {computerChoice}")
        time.sleep(2)
        print (random.choice(computerCelebrations))
        choosingAgain()

start()

