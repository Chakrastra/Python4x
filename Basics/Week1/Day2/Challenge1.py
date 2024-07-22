#Creating a Number Guessing Game using Python!

import random as r 

number = r.randint(1, 100)

print("\nWELCOME TO THE NUMBER GUESSING GAME!")
print("Can you guess the secret number between 1 and 100?")
while True:
    guessed_number = int(input("Enter your guess: "))
    while number != guessed_number:
        print("Nope, that's not the number.")
        if guessed_number > number + 10:
            print("Way too High! Come on, you can do better!")
        elif guessed_number < number - 10:
            print("Way too Low! Are you even trying?")
        elif guessed_number > number:
            print("Close, but still your number is High. Try again!")
        elif guessed_number < number:
            print("Close, but still your number is Low. Keep guessing!")

        guessed_number = int(input("Enter your guess: "))
    if number == guessed_number:
        print("Congratulations! You guessed it right!")
        print("You WIN!!! 🥳🎉")
        break





















