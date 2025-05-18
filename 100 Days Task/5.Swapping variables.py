a = 10
b = "banana"

c=b
b=a
a=c
print(f'a is {a} and b is {b}')

#gpt Tuple unpacking method

# Initial values
a = 5
b = 10

# Swap using tuple unpacking
a, b = b, a

print("After swapping: a =", a, "b =", b)
