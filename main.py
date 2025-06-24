
import random 

choices = ["rock","paper", "scissors"]
print(choices)
while True:
    print("press 4 to exit program")
    answer = input("What do you want to chose? ").lower
    # aswer validation
    while answer!= "rock" or answer!="paper" or answer !="scissors":
        print("Wrong input, try again")
        answer = input("What do you want to chose? ").lower

    random_choice = choices.random 

    if random_choice == answer:
        print("Tie!")
    #rock 
    if answer == "rock" and random_choice == "paper":
        print("You won!")
    if answer == "rock" and random_choice == "scissors":
        print("You lost.")

    #paper
    if answer == "paper" and random_choice == "rock":
        print("You won!")
    if answer == "paper" and random_choice == "scissors":
        print("You lost.")

    #scissors
    if answer == "scissors" and random_choice == "paper":
        print("You won!")
    if answer == "scissors" and random_choice == "rock":
        print("You lost.")

    #exut program
    if answer == 4:
        print("Leaving...")
        exit()
