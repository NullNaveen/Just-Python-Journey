# Try1
'''
def AoC():
    A = (22/7)*(r**2)
    return A

r = int(input("Enter the radius: "))
AoC()
'''

# gpt correct but this result is not accurate

def AoC():
    A = (22/7)*(r**2)
    return A

r = int(input("Enter the radius: "))
print("Area of the circle", AoC())

print("-----------------------------")

import math

def AoC(r):
    A = math.pi * (r ** 2)
    return A

r = int(input("Enter the radius: "))
print("Area of the circle:", AoC(r))


print("-----------------------------")
# Define a function to calculate the area of a circle
def calculate_area(radius):
    pi = 3.14159  # Approximate value of π
    area = pi * radius ** 2
    return area

# Input: radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Call the function and display the result
area = calculate_area(radius)
print("The area of the circle is:", area)

print("-----------------------------")

# Approximate value of π
pi = 3.14159

# Input: radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate area
area = pi * radius ** 2

# Display the result
print("The area of the circle is:", area)