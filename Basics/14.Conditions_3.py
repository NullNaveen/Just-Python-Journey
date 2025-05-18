SpamWords = "Click this", "Buy this", "Urgent"
print(type(SpamWords))
UserInput = input(("Enter your message: "))
if any(i in UserInput.capitalize() for i in SpamWords):
    print("This is a spam")
else:
    print("This is not a scam")

'''
# Define a list of spam words to be checked in the user input
SpamWords = ["Click this", "buy this", "Urgent"]

# Get the user input message
UserInput = input("Enter your message: ")

# Check if any of the spam words are in the user input
if UserInput:
    if any(spam_word in UserInput for spam_word in SpamWords):
        # Print the message if the input contains any spam word
        print("This is a spam")
    else:
        # Print the message if the input is not a spam
        print("This is not a scam")
else:
    # Print a helpful message if the user entered an empty input
    print("Please enter a non-empty message")

'''