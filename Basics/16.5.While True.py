while True:
    user_input = input("Enter something (type 'quit' to stop): ")
    if user_input == "quit":
        print("Exiting the loop.")
        break  # Exit the loop
    print(f"You entered: {user_input}")

#In this example, the loop will continue indefinitely, repeatedly asking for input, until the user types "quit". At that point, break stops the loop.