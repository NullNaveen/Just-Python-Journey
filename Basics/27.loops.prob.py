# for Num in range(10):
#     if Num%2 == 0:
#         print(Num, "is an even number")
#     elif Num%2 == 1:
#         print(Num, "is a odd number")

Num = int(input("Enter any Numer: "))

for i in range(2, Num):
    if Num%i == 0:
        print(Num, 'is a not prime Number')
        break
else:
    print(Num, 'is a prime Number')


#find the sum of first n natural numbers
num=int(input('Enter any number: '))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print(f"The sum of first {num} natural number is {sum}")
