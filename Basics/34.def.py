def greet(name):  #function with arguments, here it is name
    '''This function greet others'''
    print("hello "+name) #if we use plus in print func, we need to add space between strings/values

greet("John")

print(greet.__doc__)

def paraseparator():
    print('-----------------------')
paraseparator()
def greet2(name):
    return "Hello, {}".format(name)
a = greet2("Jane")
print(a)
print(greet2("Jim"))

paraseparator()

def GreetingAGirl(name="Vindhu"): #funtion with default parameter
    print("hello Chellam!",name)  #if we use comma(,) in print statement, then we dont need to add space between values

GreetingAGirl()
GreetingAGirl("Cute ponnu")   #we can also change the default parameter

paraseparator()

def average(a, b, c ,d):
    '''Calculate the average of four numbers'''
    return (a + b +c+ d)/4
x = average(10, 45, 75, 100)
print(x)

paraseparator()

def average(a, b, c ,d):
    '''Calculate the average of four numbers'''
    return (a + b +c+ d)/4
print(average(10, 45, 75, 100))

