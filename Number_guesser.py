import random

play_again = True


def ask_play_again():
        again = input("Do you want to play again? ")
        if again == "yes":
            return True
        else:
            print("Ending Game")
            return False
def get_guess():
    while True:
        raw_input = input("Guess a number: ")
        if raw_input == "exit":
            print("Exiting Game")
            exit()
        try:
            guessed_number = int(raw_input)
            return guessed_number
        except ValueError:
            print("Please enter a valid number")
def difficulty():
    
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
            return chances
        else: 
            print("Please pick a valid option")
            difficulty_level = str(input("Please select a difficulty level (easy/medium/hard): "))
def main_loop(chances):
    attempts = 0
    while chances > 0:
        guessed_number = get_guess()
            
        if guessed_number != random_number:
            if guessed_number > random_number:
                print(f"Wrong Number, the number is less than {guessed_number}")
            elif guessed_number < random_number:
                print(f"Wrong Number, the number is more than {guessed_number}")
            chances -= 1
            attempts += 1
        else:
            print(f"Well Done, you guessed the number in {attempts} attempts")
            return ask_play_again()

    if chances == 0:
        print("Sorry, you lose!")
        return ask_play_again()


while play_again:

    print("Welcome to the Number Guesser!!")
    print("I'm thinking of a number bettwen 1 and 100.")
    print("You have to guess this number. \n")

    random_number = random.randint(1, 100)


    chances = int(difficulty())
    play_again = main_loop(chances)


    

