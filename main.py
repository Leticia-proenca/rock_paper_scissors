
import random 

choices = ["rock","paper", "scissors"]
user = 0
computer = 0

while True:
    print("1- Rock \n2- Paper \n3- Scissors \n4- Score \n5-Exit")
    answer = int(input("What do you want to chose? "))
    #answer validatiom
    while answer > 5 or answer < 1:
        print("Wrong input, try again")
        answer = int(input("What do you want to chose? "))

    random_choice = random.choice(choices) 
    print(f"Computer choice: {random_choice}")

        #rock 
    while answer == 1:
        if random_choice == "paper":
            print("You won!\n")
            user += 1
        if random_choice == "scissors":
            print("You lost!\n")
            computer += 1
        if random_choice == "rock":
            print("Tie!\n")

        #paper
    while answer == 2:
        if random_choice == "rock":
            print("You won!\n")
            user += 1
        if random_choice == "scissors":
            print("You lost\n")
            computer += 1
        if random_choice == "paper":
            print("Tie!\n")

        #scissors
    while answer == 3:
        if random_choice == "paper":
            print("You won!\n")
            user += 1
        if random_choice == "rock":
            print("You lost\n")
            computer += 1
        if random_choice == "scissors":
            print("Tie!\n")

    if answer == 4:
        print("SCORES")
        print(f"User= {user}")
        print(f"Computer = {computer}\n")

        #exit program
    if answer == 5:
        print("Leaving...")
        exit()
