# Find the Maximum/Minimum in a List: Write a function to find the max and min values in a list.

MyList = [1,3,6,2,5.5]

print(max(MyList))
print(min(MyList))

def max_min(MyList):
    print(f'Maximum value is {max(MyList)}')
    print(f'Minimum value is {min(MyList)}')

max_min(MyList)

#gpt

def find_max_min(my_list):
    # Check if the list is empty
    if not my_list:
        return None, None  # Return None for both if the list is empty

    max_value = max(my_list)  # Find the maximum value
    min_value = min(my_list)  # Find the minimum value

    return max_value, min_value  # Return both values

# Example usage
my_list = [10, 20, 4, 45, 99]
max_value, min_value = find_max_min(my_list)
print(f"Maximum: {max_value}, Minimum: {min_value}")
