#while loop
num = 3
i = 1
temp = num
while temp > 1:
    i = temp * i
    temp -= 1

print(f"The factorial of {num} is {i}")

# for loop

factorial = 1
for m in range(1,num+1):
    factorial *= m

print(f"The factorial of {num} is {factorial}")