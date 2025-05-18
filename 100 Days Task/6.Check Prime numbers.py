#this code has a prob, check for 21

num = int(input("Enter a number: "))

if num == 1 or 0:
    print("Neither prime nor composite")

elif num == 2:
    print("Prime")

elif num%2 == 0:
    print("Composite")
else:
    print("Prime")

# finally victory

num = 21

for i in range(2, num):
    if num == 0 or num == 1:
        print(f"{num} is neither prime not composite")
    elif num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
