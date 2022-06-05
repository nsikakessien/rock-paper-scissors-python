import random

while True:
    print('Welcome to rock, paper and scissors')
    user_action = input("Enter a choice (R, P, S): ")
    user_action = user_action.lower()
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    computer_action = computer_action.lower()
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie! Let's play again")
    elif user_action == "r":
        if computer_action == "s":
            print("Rock beats scissors! You win!")
            break
        else:
            print("Paper beats rock! You lose.")
            break
    elif user_action == "p":
        if computer_action == "r":
            print("Paper beats rock! You win!")
            break
        else:
            print("Scissors beats paper! You lose.")
            break
    elif user_action == "s":
        if computer_action == "p":
            print("Scissors beats paper! You win!")
            break
        else:
            print("Rock beats scissors! You lose.")
            break
    else: 
        print("There is an error in your input. try again")