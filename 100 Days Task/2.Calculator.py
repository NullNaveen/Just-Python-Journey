# Try 1
Operation = int(input('''Pick the operation from below 
1. Addition
2. Subraction
3. Multiplication
4. Division
Enter the number of your choice: '''))
num1 =int(input("Enter the First number: ") )
num2 =int(input("Enter the second number: ") )

if Operation == 1:
    print(num1+num2)
elif Operation == 2:
    print(num1-num2)
elif Operation == 3:
    print(num1*num2)
elif Operation == 4:
    print(num1/num2)

#Try 2: by gpt

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input! Please enter numbers.")
    else:
        print("Invalid choice! Please select a valid operation.")

calculator()


# Take 3: Gpt : To keep asking the user for input until they enter valid choices and numbers, we can use while loops

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_operation():
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            return choice
        else:
            print("Invalid choice! Please enter a valid operation.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("This is not a valid number! Please enter a valid number.")

def calculator():
    while True:
        choice = get_operation()
        
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

        # Ask if the user wants to perform another calculation
        cont = input("\nWould you like to perform another calculation? (yes/no): ")
        if cont.lower() != 'yes':
            print("Goodbye!")
            break

calculator()
