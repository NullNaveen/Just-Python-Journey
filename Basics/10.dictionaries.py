# Dictionaries are unordered collections of key-value pairs. They are used to store data in a way that allows you to quickly and efficiently retrieve values based on their associated keys.
# Each key in a dictionary must be unique.
# Dictionaries are created by enclosing comma-separated key-value pairs within curly braces { }, with a colon : separating each key from its value.


MyFavoutireDictionaries = {
    "You": "me",
    'hi': 'hello',
    "My life": 'I hate it',
    1: {2, 3},
    list: [1,4,6],
    "Numbers":3 , 
    "word":'apple'
}
def Translate(word):
    if word in MyFavoutireDictionaries.keys():
        return MyFavoutireDictionaries[word]
    else:
        return None
print(Translate("You")) # should print "me"
print(Translate(MyFavoutireDictionaries['hi']), end=" ") # should print "hello"
print(Translate(list), Translate(1))

print(MyFavoutireDictionaries[list]) # will raise a KeyError because lists are not allowed as keys in dictionarie
print(MyFavoutireDictionaries.get(1))
print(MyFavoutireDictionaries.get(5, 10))

print(MyFavoutireDictionaries.items( ))
print(type(MyFavoutireDictionaries.items( )))
print(type(MyFavoutireDictionaries))
print(MyFavoutireDictionaries.keys())
print(type(MyFavoutireDictionaries.keys()))
print(MyFavoutireDictionaries.values())
print(type(MyFavoutireDictionaries.values()))

for a, b in MyFavoutireDictionaries.items():
    print(a, ":=", b)

print(len(MyFavoutireDictionaries))

print(MyFavoutireDictionaries.update({9:"nine", 'My life':'I fucking hate it'}))
print(MyFavoutireDictionaries.get(9, 'My life'))
print(MyFavoutireDictionaries.get('My life', 9))