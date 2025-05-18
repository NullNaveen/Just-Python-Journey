
print('--------break-------')

for i in range(5):
    print(i)
    print("\n\n")
    if i == 3:
        break  #  Exit loop when i is equal to 3.
    print("This is a test.")
else:
    print('I am bored')
    
print('----------Continue---------')

for i in range(5):
    print(i)
    if i == 3:
        continue # Skip the loop when i is equal to 3.
    print("This is a test.")
else:
    print('I am bored')

print('-----------Pass--------')
# pass is a null statement, it just do nothing
# The pass statement is used when a statement is required syntactically but you do not want any command or code executed. It can also be

if 8>3:
    # To be implemented later
    pass

for u in range(3,3,3):
    pass

def my_function():
    pass

class MyClass:
    pass

class AbstractClass:
    def my_method(self):
        # This method is meant to be overridden
        pass
