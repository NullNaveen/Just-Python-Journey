
# write a program to print multiplication table of a given number using for loop
Num =  int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{i}x{Num} = {i*Num}")

# another way to do the same task by taking two numbers as input and printing their multiplication tables.
Nums = list(map(int, input("Enter two numbers separated by space :").split()))
print("\nMultiplication Table of First Number")
for i in range(1, 11):
    print(f"{i} x {Nums[0]} = {i * Nums[0]}")

print("\nMultiplication Table of Second Number")
for j in range(1, 11):
    print(f"{Nums[1]} x {j} = {Nums[1] * j}\n")

#using while loop

Num2 =  int(input("Enter the number: "))
i=1
while i <= 10:
    print(f"{i} x { Num2} = {i*Num2}")
    i += 1

#write multiplication table in reverse order    
n=4
for i in range(1,11):
    i=11-i
    print(f'{i} X {n} = {i*n}')
