def func1():
    print("Hello Mutta payaley")
    print("Hello da Dhomma")

func1()
func1()
func1()

print('=============')

def fun1():
    print("fun1")

def fun2(a, b):
    return a + b

print(fun2.__name__)  # Output: fun2
print(fun1.__name__)   # Output: fun1

# You can also use the __doc__ attribute to get documentation strings.
print(fun2.__doc__)     # Output: Return a+b.
print(fun1.__doc__)           # Output: None
# The __module__ attribute of functions gives you access to the module in which they were defined.
print(fun2.__module__)       # Output: __main__ (or whatever your script is named).
print(fun1.__module__)                   # Output: __main__

# Functions are first-class objects in Python. This means that function names can be used as variables and vice versa.
# Functions are first-class objects in Python, meaning that they can be assigned to variables and passed as arguments to other functions.

