n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("*"*i)

print("hi"*5,end=(","))
print("hi"*5,end=(""))
print("hi"*5,end=("\n"))
print("hi"*5,sep=(","))


def print_right_angle_pattern(rows):
    """
    Function to print a right-angled pattern of asterisks.

    Parameters:
        rows (int): Number of rows in the pattern.

    Returns:
        None
    """
    for i in range(1, rows + 1):  # Outer loop for rows
        print("*" * i)            # Print asterisks for the current row

# Example usage:
rows = int(input("Enter the number of rows: "))
print_right_angle_pattern(rows)
