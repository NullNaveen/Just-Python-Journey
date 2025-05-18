import random

# Generate a random number between 1 and 100
guess_the_number = random.randint(1, 100)

while True:
    # Ask the user to guess the number
    user_input = int(input("Guess the number between 1-100:\n"))
    
    # Check if the guess is correct
    if user_input == guess_the_number:
        print("You got it right!")
        break
    elif user_input < guess_the_number:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")


'''
#Ask the user to guess the number until they get it right

#To make it more interesting, let’s try to guess a number between 1 and 100 using only one line of code:
import random
guess_the_number = random.randint(1, 100)
while True:
    user_input = int(input("Guess the number between 1-100:\n"))
    if user_input == guess_the_number:
        break
    elif user_guess < guess_the_number:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
print("You got it right!")
'''