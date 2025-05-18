#printing star pattern

n = 5  # number of rows to be printed
c = 1  # value of 'c' is initialized as 1

print("Entered number of rows:", end=" ")
n = int(input())  # taking user input for number of rows

for i in range(1, n + 1):  # loop will iterate till 'n'
    for c in range(1, i + 1):  # inner loop to print the stars
        print("*", end="")
    print()  # printing a new line after each row

print('---------------------------')

import time
for i in range(1,n+1):
    if (i%2==0):
        c=63-c   # decrementing the value of 'c' when 'i' is even.
    else:
        c+=9   # incrementing the value of 'c' when 'i' is odd.
    
    print("\033[{}F".format(i),end="")  # \033[2J - clear screen
                                         # \033[{}F - move cursor to beginning of the line
    time.sleep(.1)               # delay of .1 seconds 

