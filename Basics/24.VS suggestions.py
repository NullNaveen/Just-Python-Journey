
    
# 1. Write a Python program that prints the numbers from 0 to  9 using nested loops. The outer loop should run 3 times and the inner loop should also
# 2. Write a Python program that takes two numbers as input from the user and prints their sum, difference, product and quotient.
#Exercise 2: Create a program that prompts the user to enter their name and then prints out a welcome message with their name
# 1. Write a Python program that prints the numbers from 0 to 9 using nested loops.
# 2. Modify your program so it only prints odd numbers and skips even numbers.
# 3. Use one loop to control another loop instead of having two separate loops.

for num in range(10): # outer loop controls how many times inner loop will run
    if (num % 2) == 1: # checks if number is odd, returns True or False
        for _ in range(abs(num // 2)): # inner loop runs abs(num//2) times because we want to multiply by 0.5 not divide
            for _ in range(abs(num // 2)): # inner loop runs abs(num//2) times because we want to multiply by 2 each time
                print(num)
        
print()

# Now let's try question  3 with a single loop

for num in range(1,  11): # we start from 1 because range function doesn't include the starting number by default
    for num in range(1, 11): # start at 1 and end at 10 (not including 10), so we have 10 iterations
        if (num % 2) != 0: # checks if number is not divisible by 2, which means it's an odd number
            print(num)
        