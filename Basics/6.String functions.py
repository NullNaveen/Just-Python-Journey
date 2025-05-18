#There are three types of string quotes 
#1. Single Quotes: 'Hello World'
#2. Double qoutes: "Hello World"
#3. Triple qoutes: '''Hello World'''


Yo= 'This life is seriously fucking boring'
print(len(Yo))
print(Yo.endswith("ing"))
print(Yo.startswith('This'))
print(Yo.find('life'))
print(Yo.replace('fuck','shit'))
print(Yo.count("i"))
print(Yo.count("is"))
print(Yo.count("z"))
print(Yo.capitalize())

class Person():
    def __init__(self,name):
        self.name = name
    def greet(self):
        return f"Hi {self.name}!"
PersonOne = Person("John")
print(PersonOne.greet())

print(Yo[0])
print(Yo[-5:-1])
print(Yo[:6])
print(Yo[7:])

#Slicing a string with step parameter
print(Yo[::1])     #Normal slicing
print(Yo[::-1])    #Reverse Slicing
print(Yo[::2])         #Skipping every other character in the string
print(Yo[1::2])       #Start from second char and skipping every other character


#Checking if something exists in a string using in keyword
def check_string(word,sentence):
    if "boring" in Yo:
        return True
    else:
        return False