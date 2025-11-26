#import random module for guessing game
import random
play_again = "Y"

while play_again == "Y":
    # Introduction and user selects and upper limit for guessing game
    name = input('Welcome to the number guessing game! Please enter your name to begin: ')
    upper_limit = int(input(f'Thank you, {name}! Pick an upper limit to set as the maximum number the game can choose: '))

    #computer picks a random number from 1-users selected upper limit
    random_number = random.randint(1,upper_limit)

    #user  tries to guess the number
    correct_guess = False

    guess_counter = 0
    while not correct_guess: 
        number_guess = int(input('Now try to guess the number: '))
        if number_guess == random_number:
            print('Correct!')
            correct_guess = True
            guess_counter = guess_counter + 1
        elif number_guess > random_number:
            print('Too high!')
            guess_counter = guess_counter + 1
        elif number_guess < random_number:
            print('Too low!')
            guess_counter = guess_counter + 1

    if guess_counter > 1:
        print(f"Nice job, {name}! You guessed the number in {guess_counter} tries.")
    elif guess_counter == 1:
        print(f"Nice job, {name}! You guessed the number in {guess_counter} try")
    play_again = input('Would you like to play again? (Enter Y/N): ') 
