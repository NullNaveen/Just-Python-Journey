a=5
b=4
c=2

#Arithmetic operator
print(a+b)
print(a*b)
print(a-b)
print(a/b)

#Assignment operators
a += 5
b-=3
c *= 10
print(a)
print(b)
print(c)
 
#Comparison operators 
print(a==b)
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a!=c/2)

# Logical Operators: and, or, not
print(a==b and  b==c) #True if both are true
print(a==b or  b==c) #True if any one is True
print(not (a==b))     #Negation of the expression. It returns False if condition is True else it returns True





# 1. **Arithmetic Operators**:
#    - Addition `+`: Adds two operands.
#    - Subtraction `-`: Subtracts the right operand from the left operand.
#    - Multiplication `*`: Multiplies two operands.
#    - Division `/`: Divides the left operand by the right operand (always results in a float).
#    - Floor Division `//`: Divides and rounds down the result to the nearest integer.
#    - Modulus `%`: Returns the remainder of the division of the left operand by the right operand.
#    - Exponentiation `**`: Raises the left operand to the power of the right operand.

# 2. **Comparison Operators**:
#    - Equal to `==`: True if the operands are equal.
#    - Not equal to `!=`: True if the operands are not equal.
#    - Greater than `>`: True if the left operand is greater than the right operand.
#    - Less than `<`: True if the left operand is less than the right operand.
#    - Greater than or equal to `>=`: True if the left operand is greater than or equal to the right operand.
#    - Less than or equal to `<=`: True if the left operand is less than or equal to the right operand.

# 3. **Assignment Operators**:
#    - Assignment `=`: Assigns a value to a variable.
#    - Add and assign `+=`: Adds the right operand to the left operand and assigns the result to the left operand.
#    - Subtract and assign `-=`: Subtracts the right operand from the left operand and assigns the result to the left operand.
#    - Multiply and assign `*=`: Multiplies the left operand by the right operand and assigns the result to the left operand.
#    - Divide and assign `/=`: Divides the left operand by the right operand and assigns the result to the left operand.
#    - Floor divide and assign `//=`: Divides the left operand by the right operand, rounds down, and assigns the result to the left operand.
#    - Modulus and assign `%=`: Computes the modulus of the left operand with the right operand and assigns the result to the left operand.
#    - Exponentiate and assign `**=`: Raises the left operand to the power of the right operand and assigns the result to the left operand.

# 4. **Logical Operators**:
#    - Logical AND `and`: Returns True if both operands are true.
#    - Logical OR `or`: Returns True if either of the operands is true.
#    - Logical NOT `not`: Returns True if the operand is false.

# 5. **Identity Operators**:
#    - Identity `is`: Returns True if both operands are the same object.
#    - Not Identity `is not`: Returns True if both operands are not the same object.

# 6. **Membership Operators**:
#    - Membership `in`: Returns True if a sequence (e.g., a string, list, tuple) contains a specified value.
#    - Not Membership `not in`: Returns True if a sequence does not contain a specified value.

# These operators are fundamental to performing various operations and comparisons in Python.


# The terms "ordered" and "unordered" refer to how the elements are stored and accessed within a collection.

# 1. **Ordered Collection**:
#    - An ordered collection maintains the order of its elements, meaning the elements are stored and accessed in a sequential manner.
#    - Lists and tuples in Python are examples of ordered collections. When you access elements in a list or tuple by index, you get the elements in the same order as they were inserted.
#    - Example:
#      ```python
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
#      ```

# 2. **Unordered Collection**:
#    - An unordered collection does not maintain the order of its elements. The elements are stored in a way that is optimized for efficient retrieval but not necessarily in the order they were inserted.
#    - Dictionaries and sets in Python are examples of unordered collections.
#    - Dictionaries use a hash table internally for storing key-value pairs, which allows for fast retrieval of values based on keys, but the order of insertion is not preserved.
#    - Sets use a hash set internally, which also does not maintain the order of elements.
#    - Example:
#      ```python
my_dict = {'name': 'Nicky', 'age': 30, 'city': 'New York'}
print(my_dict['name'])  # Output: Nicky
#      ```

# In summary, ordered collections preserve the order of elements, while unordered collections do not. Depending on your use case, you might choose one over the other based on considerations such as the need for element ordering and the efficiency of element retrieval. Let me know if you need further explanation, Nike!