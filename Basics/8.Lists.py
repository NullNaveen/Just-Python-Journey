# Lists are ordered collections of items. They can contain elements of different data types and are mutable, meaning you can change their contents after they're created.
# You can create a list by enclosing comma-separated values within square brackets [ ].

mySetOfLists = [4,5, 0o3, 76,26,90]
print(mySetOfLists)
print(type(mySetOfLists))

mySetOfLists.reverse()
print(mySetOfLists)

mySetOfLists.sort()  #Sorting the set of lists in ascending 
print(mySetOfLists)  #we can't sort if the list contains any strings or booleans

mySetOfLists.reverse()
print(mySetOfLists)

mySetOfLists.sort(reverse=True) #Sorting the set of lists in descending
print(mySetOfLists)

mySetOfLists.append(77)
print(mySetOfLists)

mySetOfLists.insert(1,"Hello")
print(mySetOfLists)

mySetOfLists.pop()
print(mySetOfLists)

mySetOfLists.pop()
print(mySetOfLists)

mySetOfLists.pop(1)
print(mySetOfLists)

mySetOfLists.remove(76)  #remove the first occurance in the list
print(mySetOfLists) 

secondlist = [88, "World", False, 88, 7.5, 88]
secondlist.remove(88)  
print(secondlist)     


secondlist.pop(0)
secondlist.pop(0)
a = secondlist.sort()
print(a)            #all list functions are updating the list not returning the value
print(secondlist)


'''
set_of_tuples = (78,96,76)
value_to_check = 76
if value_to_check in set_of_tuples:
    print(f"{value_to_check} exists in the set.")
else:
    print(f"{value_to_check} does not exist in the set.")
'''