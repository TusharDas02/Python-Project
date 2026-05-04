# Rock crushes Scissors & Lizard
# Paper covers Rock & disproves Spock
# Scissors cuts Paper & decapitates Lizard
# Lizard eats Paper & poisons Spock
# Spock smashes Scissors & vaporizes Rock




import random as r

choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

flag = True

while flag == True:

    player_choice = input("Enter your choice: Rock, Paper, Scissors, Lizard, or Spock: \n").lower() 
    computer_choice = r.choice(choices).lower()

    print(f"Computer chose: {computer_choice.capitalize()}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and (computer_choice =="scissors" or computer_choice == "lizard"):
        if computer_choice == "scissors":
            print("You win! Rock crushes Scissors.")
        else:
            print("You win! Rock crushes Lizard.")
    elif player_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock"):
        if computer_choice == "rock":
            print("You win! Paper covers Rock.")
        else:
            print("You win! Paper disproves Spock.")
    elif player_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard"):
        if computer_choice == "paper":
            print("You win! Scissors cuts Paper.")
        else:
            print("You win! Scissors decapitates Lizard.")
    elif player_choice == "lizard" and (computer_choice == "paper" or computer_choice == "spock"):
        if computer_choice == "paper":
            print("You win! Lizard eats Paper.")
        else:
            print("You win! Lizard poisons Spock.")
    elif player_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock"):
        if computer_choice == "scissors":
            print("You win! Spock smashes Scissors.")
        else:
            print("You win! Spock vaporizes Rock.") 
    else:
        print("You lose! Computer wins with " + computer_choice.capitalize() + ".")

    out = input("Write 'exit' to exit the game.").lower()

    if out == "exit":
        flag = False

