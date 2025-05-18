#The for loop iterates over a sequence (such as a list, tuple, string, or range) or any iterable object
for k in range(5):  # iterate over the numbers from  0 to 4
    print(k)

#You can also use a while loop if you don’t know how many times you want to loop.


lol = 'King'  #print a string three time, its three time because the index starts from 0 and ends at 2
for a in range(3):
    print(lol)


for  word in ["apple", "banana", "cherry"]:
    if len(word) > 5:
        print("Long word: ", word)
    else:
        print("Short word: ", word)

#You can also use the enumerate function to get both the index and value of each item in an iteration.
        
fruits = ["apple", "banana", "cherry"]

for index, word in enumerate(fruits):
    if len(word) > 5:
        print("Long word at index", index, ":", word)
    else:
        print("Short word at index", index, ":", word)


for i in fruits:
    print(i)

for i in fruits:
    print(i + " is tasty")

for i in fruits:
    print(i)
    print(i + " is tasty")
