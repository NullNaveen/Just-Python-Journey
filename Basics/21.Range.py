for i in range(5):
    print(i)

print("Done")

# Range function has three arguments
# 1. start - the value of the starting point in an iteration. (Optional, default is  0)
# 2. stop  - the value at which to stop iterating. This value is not included in the loop.
# 3.  step - how much to add/subtract each time through the loop. (Optional, default is 1)

#Example:
for i in range(0, 5, 2): #It will iterate from  0 to 4 with a step of  2 so it will print 0,  2 ,4
    print(i)


print(list(range(3)))   # [0, 1, 2]
print(tuple(range(3)))   # (0, 1, 2)
print(set(range(6)))     # {0, 1, 2,  3, 4}
print(frozenset(range(6))) # frozenset({0, 1, 2, 3,  4})

print(*range(1, 10), sep=", ")  # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9


