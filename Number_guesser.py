import random

play_again = True

while play_again:

    print("Welcome to the Number Guesser!!")
    print("I'm thinking of a number bettwen 1 and 100.")
    print("You have to guess this number. \n")

    random_number = random.randint(1, 100)


    difficulty_level = str(input("Please select a difficulty level: \n" \
                        "1. Easy (10 chances)\n" \
                        "2. Medium (5 chances) \n" \
                        "3. Hard (3 chances)\n" \
                        "\n" \
                        "Enter your choice: ")).strip().lower()

    chances = None

    game_state = {
        'easy': 10,
        'medium': 5,
        'hard': 3
    }

    while True:
        if difficulty_level in game_state:
            chances = game_state[difficulty_level]
            break
        else: 
            print("Please pick a valid option")
            difficulty_level = str(input("Please select a difficulty level (easy/medium/hard): "))

    while chances > 0:
        while True:
                raw_input = input("Guess a number: ")
                if raw_input == "exit":
                    print("Exiting the program")
                    exit()
                try:
                    guessed_number = int(raw_input)
                    break
                except:
                    print("Please enter a valid number")
            
        if guessed_number != random_number:
            if guessed_number > random_number:
                print(f"Wrong Number, the number is less than {guessed_number}")
            elif guessed_number < random_number:
                print(f"Wrong Number, the number is more than {guessed_number}")
            chances -= 1
        else:
            print("Well Done")
            again = input("Do you want to play again? ")
            if again == "yes":
                play_again = True
                break
            else:
                play_again = False
                print("Ending Game")
                break

    if chances == 0:
        print("Sorry, you lose!")
        again = input("Do you want to play again? ")
        if again == "yes":
            play_again = True
        else:
            play_again = False
            print("Ending Game")
            break