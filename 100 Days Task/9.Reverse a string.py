#Reverse a string input by the user.
#solved without knowing how

String = "Hello Macha"
RevStr = reversed(String)

for i in RevStr:
    print(i, end="")

#AMA

def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello World"))

#GPT

reversed_string = ''.join(reversed(String))
print(reversed_string)

#GPT Ultra Pro Max

# Get input from the user
user_input = input("Enter a string: ")

# Reverse the string
reversed_string = user_input[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)

