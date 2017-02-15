# Imports module needed for the "Guess the Random Number" game
import random

print("=========================")
# Makes program run forever
while True:
    print("Minigames Menu")
    print()
    print("Games:\nGuess the Random Number\n(More games will be added soon...)")
    print()
    game = input("Which game do you want to play?\n(\"G\" for \"Guess the Random Number\")\n(\"quit\" to end the program) : ")
    if game == "G" or game == "g":
# Guess the Random Number Game
        print()
        x = random.randint(0, 10)
        turns = 3
        print("You have 3 turns\nThe number is between 0 and 10")

# Makes game run forever
        while True:
            user = input("Can you guess the number:")

# Runs if the user entered the right number
            if x == int(user):
                print("You got it!")
                print("The answer was " + str(x))

# Asks user if they want to play again
                play_again = input("Would you like to play again? (Y/N): ")
                if play_again == "Y":
                    turns = 3
                    print("\nYou have 3 turns\nThe number is between 0 and 10")
                    continue
                elif play_again == "N":
                    break
                else:
                    print("Error. Invalid Input. Quitting Game")
                    break

# Runs if user enters the wrong number
            else:
                print("try again")
                turns -= 1
                print("You have " + str(turns) + " turns left")

# Ends game when user runs out of turns
            if turns == 0:
                print("The answer was " + str(x))

# Asks user if they want to play again
                play_again = input("Would you like to play again? (Y/N): ")
                if play_again == "Y":
                    turns = 3
                    print("\nYou have 3 turns\nThe number is between 0 and 10")
                    continue
                elif play_again == "N":
                    break
                else:
                    print("Error. Invalid Input. Quitting Game")
                    break
        print("=========================")

# Ends main While loop if user enters "quit"
    elif game == "quit":
        print("Program Ended")
        break
# Runs if user does not input "G" or "quit"
    else:
        print("Error. Invalid Game ID")
