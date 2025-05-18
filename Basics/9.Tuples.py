# Tuples are similar to lists but are immutable, meaning once they are created, you cannot change the elements inside them.
# Tuples are created by enclosing comma-separated values within parentheses ( ).

Tuples = (88, "World", False, 88, 7.5, 88)
print(Tuples)
print(type(Tuples))
print(len(Tuples))
print(Tuples.count(False))
print(Tuples.count(88))
print(Tuples.index(88))
a=(7) #this will consider as an integer to make it as an tuple use Comma
b=(7,)
c=()
print(type(a), type(b), type(c))


# Accessing elements of a tuple using indexing:
try:
    print("Accessing elements by index:\n")
    for i in range(0, len(Tuples)):
        print(f"Element at index {i}: {Tuples[i]}")
except IndexError as e:
    print("\nIndex Error occurred: ", str(e))

