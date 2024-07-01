#Number Guessing Game with AI

def Ai_number_guessing_game():
    print("\n\tWelcome to the Number Guessing Game with AI!")
    
    low = int(input("\nEnter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))
    
    target = int(input("Think of a number for AI to guess: "))
    
    if target < low or target > high:
        print(f"Please enter a number within the range {low} and {high}.")
        return
    
    attempts = 0
    ai_guess = None

    while ai_guess != target:
        attempts += 1
        ai_guess = (low + high) // 2  
        print(f"\nAI guesses: {ai_guess}")

        feedback = input("Is the guess too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == 'l':
            low = ai_guess + 1
        elif feedback == 'h':
            high = ai_guess - 1
        elif feedback == 'c':
            print(f"\nAI guesses correctly! It took {attempts} attempts.")
            break
        else:
            print("Invalid feedback. Please enter 'H', 'L', or 'C'.")


Ai_number_guessing_game()