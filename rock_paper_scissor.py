
import random

user_wins=0
computer_wins = 0

options = ["rock", "paper" , "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    #rock = 0 , paper = 1 , scissor = 2
    option_chosen = options[random_number]
    print("Computer picked: {} , you picked: {}".format(option_chosen,user_input))

    if(user_input == "rock" and option_chosen == "scissor"):
        print("You win!")
        user_wins += 1
        continue

    if(user_input == "rock" and option_chosen == "paper"):
        print("Computer wins, you loose!")
        computer_wins += 1
        continue

    if(user_input == "paper" and option_chosen == "scissor"):
        print("Computer wins, you loose!")
        computer_wins += 1
        continue

    if(user_input == "paper" and option_chosen == "rock"):
        print("You win!")
        user_wins += 1
        continue
    
    if(user_input == "scissor" and option_chosen == "rock"):
        print("Computer wins, you loose!")
        computer_wins += 1
        continue

    if(user_input == "scissor" and option_chosen == "paper"):
        print("You win!")
        user_wins += 1
        continue

    if(user_input == option_chosen ):
        print("Its a tie")
        continue

print("Computer won {} times, you won {} times!".format(computer_wins,user_wins))
print("Goodbye!")