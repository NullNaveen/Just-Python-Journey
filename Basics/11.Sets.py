# Sets are unordered collections of unique elements. They are useful for operations such as checking membership and finding intersections, unions, and differences between sets.
# Sets are created by enclosing comma-separated values within curly braces { }.

a={}
b=set()
c={1}
d=frozenset({3,4})

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Mysets= {a:b,"c":[1,2],"d":"hello"}
#for key in Mysets.keys():
#    print("key="+str(key)+",value="+str(Mysets[key]))

Mysets = {4,list, 'I love u', 6}
print(Mysets.add(8))
Mysets.remove(6)
print(Mysets.pop())
print(Mysets.discard('I love u'))
Mysets.discard(10)
print(Mysets)

print('-------------------')

MySets={7,8,9}
print(MySets)
print(MySets.union(Mysets))
print(MySets)
print(MySets.union(set([5,6,7])))
print(MySets.union({10,11}))
print(MySets)
print(MySets.intersection({8,9,10}))
print(MySets)

print(MySets.clear())
print(MySets)




#A=Mysets.intersection([5,6,7])
#B=Mysets.symmetric_difference({7,8,9})
#C=Mysets.difference({5,