MyList = ['hi', {4,5}, 4, 'wtf', {"Meow": "Woof"}];
i = 0
while i < len(MyList):
    print(MyList[i])
    i += 1

print("1------------------------------")


for i in range(len(MyList)):
    print(MyList[i])
    i += 1
print('2---------------------------------')   

for item in MyList:
    print(item)

print("3------------------------------")

for sfafjkaf in MyList:
    print(sfafjkaf)

print("4------------------------------")

for  key, value in MyList[-1].items():
    print("{}: {}".format(key,value))

print('5-----------------------------')
# This will not work because we are trying to modify a tuple while iterating over it.
try:
    for j in range(len(MyList[1])):
        MyList[1][j] *= 2
except TypeError as e:
    print(e)

print("6------------------------------")


