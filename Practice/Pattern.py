rows=3
for i in range(1,rows+1):
    print("*" * i)

print()

for i in range(1, rows + 1):
    # Print spaces to center the triangle
    print(" " * (rows - i), end="")
    # Print asterisks with spaces in between for the triangle shape
    print("* " * i)
    