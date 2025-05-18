import random
# Accessing the docstring of the random module
# print(random.__doc__)

choices = ("Stone", "Paper", "Scissor")
computer = random.choice(choices)
# computer = random.randint(0,2)
# computer = choices[computer]
Player = input("Pick one: Stone or Paper or Scissor:- ").capitalize()


if Player not in choices:
    print("Dei, Dhomma\n\tSelect a valid choice da")
else:
    print(f"You chose {Player} and Bot chose {computer}")
    if Player == computer:
        print("Tie")
    elif (Player == "Scissor" and computer == "Paper") or\
        (Player == "Stone" and computer == "Scissor") or\
        (Player == "Paper" and computer == "Stone"):
        print("Hurray!🥳 You win")
    else:
        print("😔 Bot wins👎")