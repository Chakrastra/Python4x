# Write a Python program to simulate a Rock-Paper-Scissors game using functions.
import random
def get_user_choice():
    while True:
        user_choice = input("\nEnter your choice (rock/paper/scissors): ")
        if user_choice.lower() in ["rock", "paper", "scissors"]:
            return user_choice.lower()
        else:
            print("Invalid choice.")

def get_computers_choice():
    choices = ["rock", "paper", "scissors"]
    comp=random.choice(choices)
    print(f"\nComputer chooses:{comp}")
    return comp

def determine_winner(user_choice,computers_choice):
    if user_choice==computers_choice:
        return "It's a tie."
    elif (user_choice == 'rock' and computers_choice == 'scissors') or \
        (user_choice == 'paper' and computers_choice == 'rock') or \
        (user_choice == 'scissors' and computers_choice == 'paper'):
        print("\n\tYou win this round!")
        return 'You'
    else:
        print("\n\tComputer wins this round!")
        return 'Computer'
def Game():
    user= 0
    computer= 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computers_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == 'You':
            user+= 1
        elif winner == 'Computer':
            computer+= 1

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Final Score: \nYou: {user} \nComputer: {computer}")
    print("Thanks for playing!")
print("\n\t Rock Paper Scissors game! \t\n ") 
Game()


    
   
    



