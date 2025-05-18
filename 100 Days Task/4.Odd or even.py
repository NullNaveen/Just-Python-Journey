num = int(input("Enter a number: "))

if num%2 == 0:
    print("Even")
elif num%2 == 1:
    print("Odd")

#gpt
#Your code will work correctly for most numbers, but it will not handle negative odd numbers properly. When num is negative (e.g., -1), the remainder of num % 2 is -1, not 1. This causes the code to skip the elif condition, so it won’t output "Odd" for negative odd numbers.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
